/* jshint asi: true */

var addon = require('./build/Release/node-anonize-relic')
var underscore = require('underscore')


var Registrar = function (s) {
  var p

  if (!(this instanceof Registrar)) return new Registrar(s)

  if (!s) {
    this.parameters = addon.makeKey()
    return
  }

  if (typeof s !== 'string') s = JSON.stringify(s)
  p = JSON.parse(s)
  if ((typeof p.registrarSK !== 'string') || (typeof p.registrarVK !== 'string')) throw new Error('invalid JSON: ' + s)

  this.parameters = underscore.pick(p, [ 'registrarSK', 'registrarVK' ])
}

Registrar.prototype.toJSON = function () {
  return this.parameters
}

Registrar.prototype.publicInfo = function () {
  return underscore.pick(this.parameters, [ 'registrarVK' ])
}

Registrar.prototype.register = function (request) {
  var info = parseStr(request, 'registrar request',
                      '==========ANONLOGIN_CRED_BEG==========', '==========ANONLOGIN_CRED_END===========')

  return addon.registerServerResponse(info[0][0], request, this.parameters.registrarSK)
}


var Surveyor = function (s) {
  var p

  if (!(this instanceof Surveyor)) return new Surveyor(s)

  if (!s) return

  if (typeof s !== 'string') s = JSON.stringify(s)
  p = JSON.parse(s)
  if ((typeof p.surveyorId !== 'string') || (typeof p.surveyVK !== 'string') || (typeof p.registrarVK !== 'string') ||
      ((typeof p.surveySK !== 'string') && (typeof p.surveySK !== 'undefined')) ||
      ((typeof p.signature !== 'string') && (typeof p.signature !== 'undefined'))) throw new Error('invalid JSON: ' + s)

  this.parameters = underscore.pick(p, [ 'surveyorId', 'surveyVK', 'registrarVK', 'surveySK', 'signature' ])
}

Surveyor.prototype.initialize = function (registrarVK) {
  if (this.parameters) throw new Error('invalid initialization')

  this.parameters = addon.createSurvey()
  this.parameters.surveyorId |= this.parameters.surveyId
  delete(this.parameters.surveyId)
  this.parameters.registrarVK = registrarVK

  return this
}

Surveyor.prototype.toJSON = function () {
  return (this.parameters || {})
}

Surveyor.prototype.publicInfo = function () {
  return underscore.pick(this.parameters, [ 'surveyorId', 'surveyVK', 'registrarVK' ])
}

Surveyor.prototype.sign = function (userId) {
  userId = uId(userId)

  return addon.extendSurvey(this.parameters.surveyorId, this.parameters.surveyVK, this.parameters.surveySK, userId)
}

Surveyor.prototype.verify = function (request) {
  var s = addon.verifyMessage(request, this.parameters.registrarVK, this.parameters.surveyorId, this.parameters.surveyVK)

  try { s = JSON.parse(s) } catch(ex) { }
  return s
}


var Credential = function (userId, registrarVK) {
  var p, s

  if (!(this instanceof Credential)) return new Credential(userId, registrarVK)

  if (!userId) throw new Error('missing parameters')
  userId = uId(userId)

  if ((typeof userId === 'string') && (typeof registrarVK === 'string')) {
    this.parameters = { userId: userId, registrarVK: registrarVK }
    return
  }
  if (typeof registrarVK !== 'undefined') throw new Error('invalid parameters')

  s =  (typeof userId !== 'string') ? JSON.stringify(userId) : userId
  p = JSON.parse(s)
  if ((typeof p.userId !== 'string') || (typeof p.registrarVK !== 'string')) {
    throw new Error('invalid JSON: ' + s)
  }

  this.parameters = underscore.pick(p, [ 'userId', 'registrarVK', 'masterUserToken' ])
}

Credential.prototype.toJSON = function () {
  return this.parameters
}

Credential.prototype.request = function () {
  this.parameters.preFlight = addon.makeCred(this.parameters.userId)
  return addon.registerUserMessage(this.parameters.preFlight, this.parameters.registrarVK)
}

Credential.prototype.finalize = function (response) {
  if (!this.parameters.preFlight) throw new Error('preFlight missing for credential')

  this.parameters.masterUserToken = addon.registerUserFinal(this.parameters.userId, response, this.parameters.preFlight,
                                                            this.parameters.registrarVK)
  delete(this.parameters.preFlight)

  return this
}

Credential.prototype.submit = function (survey, message) {
  if (!this.parameters.masterUserToken) throw new Error('masterUserToken missing for credential')

  if (typeof message === 'undefined') message = {}
  if (typeof message !== 'string') message = JSON.stringify(message)

  return addon.submitMessage(message, this.parameters.masterUserToken, this.parameters.registrarVK,
                             survey.parameters.signature.split(',')[1].trim(),
                             survey.parameters.surveyorId, survey.parameters.surveyVK)
}


var parseStr = function (s, text, header /*, trailer */) {
  var a, x, z

  z = s.trim()
  x = z.indexOf(header)
/*
  if (x === -1) throw new Error('invalid ' + text + ' header: ' + s)
  z = z.substring(x + header.length).trim()
  x = z.indexOf(trailer)
  if (x === -1) throw new Error('invalid ' + text + ' trailer: ' + s)
  z = z.substring(0, x - 1)
 */

  a = []
  z.trim().split('\n').forEach(function (line) { a.push(line.trim().split(' ')) })

  return a
}

var uId = function (s) {
  if (typeof s !== 'string') return s

  var u = s.split('-').join('')
  return ((u.length !== 32) || (u.substr(12, 1) !== '4')) ? s : u
}


module.exports =
  { version: addon.version,
    Registrar: Registrar,
    Surveyor: Surveyor,
    Credential: Credential
  }
