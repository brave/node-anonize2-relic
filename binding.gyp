{
  "targets"         : [
    {
      "target_name" : "node-anonize-relic",

      "defines" : [
        "NDEBUG",
        "RELIC_LIBRARY",
        "ARCH=X64",
        "ALIGN=16",
        "COLOR=OFF",
        "SEED=UDEV",
        "WITH=BN;DV;FP;FPX;EP;EPX;PP;MD",
        "BN_PRECI=256",
        "BN_MAGNI=DOUBLE"
       ],

      "include_dirs" : [
        "anonize2/relic/include",
        "anonize2/relic/include/low",
        "anonize2/relic-build/include"
       ],

      "conditions": [
        [ "OS=='linux'", {
          "sources"     : [
            "anonize2/addon.cc",

            "anonize2/anon.cpp",
            "anonize2/sha2.cpp"
           ],

          "cflags_cc" : [
            "-std=c++11",
            "-g",
            "-O1",
            "-fomit-frame-pointer",
            "-msse2",
            "-mfpmath=sse",
            "-march=native"
          ],


          "ldflags": [
            "-L./src/relic-build/lib"
          ],
          "libraries": [
            "../src/relic-build/lib/librelic.so"
          ]
        }],

        [ "OS=='mac'", {
          "sources"     : [
            "anonize2/addon.cc",

            "anonize2/anon.cpp",
            "anonize2/sha2.cpp",

            "anonize2/relic/src/relic_err.c",
            "anonize2/relic/src/relic_core.c",
            "anonize2/relic/src/relic_conf.c",
            "anonize2/relic/src/relic_pool.c",
            "anonize2/relic/src/relic_util.c",
            "anonize2/relic/src/arch/relic_arch_x64.c",
            "anonize2/relic/src/rand/relic_rand_core.c",
            "anonize2/relic/src/rand/relic_rand_hash.c",
            "anonize2/relic/src/bn/relic_bn_add.c",
            "anonize2/relic/src/bn/relic_bn_cmp.c",
            "anonize2/relic/src/bn/relic_bn_div.c",
            "anonize2/relic/src/bn/relic_bn_factor.c",
            "anonize2/relic/src/bn/relic_bn_gcd.c",
            "anonize2/relic/src/bn/relic_bn_lcm.c",
            "anonize2/relic/src/bn/relic_bn_mem.c",
            "anonize2/relic/src/bn/relic_bn_mod.c",
            "anonize2/relic/src/bn/relic_bn_mul.c",
            "anonize2/relic/src/bn/relic_bn_mxp.c",
            "anonize2/relic/src/bn/relic_bn_prime.c",
            "anonize2/relic/src/bn/relic_bn_rec.c",
            "anonize2/relic/src/bn/relic_bn_shift.c",
            "anonize2/relic/src/bn/relic_bn_smb.c",
            "anonize2/relic/src/bn/relic_bn_sqr.c",
            "anonize2/relic/src/bn/relic_bn_srt.c",
            "anonize2/relic/src/bn/relic_bn_util.c",
            "anonize2/relic/src/dv/relic_dv_mem.c",
            "anonize2/relic/src/dv/relic_dv_util.c",
            "anonize2/relic/src/fp/relic_fp_add.c",
            "anonize2/relic/src/fp/relic_fp_cmp.c",
            "anonize2/relic/src/fp/relic_fp_exp.c",
            "anonize2/relic/src/fp/relic_fp_inv.c",
            "anonize2/relic/src/fp/relic_fp_mul.c",
            "anonize2/relic/src/fp/relic_fp_param.c",
            "anonize2/relic/src/fp/relic_fp_prime.c",
            "anonize2/relic/src/fp/relic_fp_rdc.c",
            "anonize2/relic/src/fp/relic_fp_shift.c",
            "anonize2/relic/src/fp/relic_fp_sqr.c",
            "anonize2/relic/src/fp/relic_fp_srt.c",
            "anonize2/relic/src/fp/relic_fp_util.c",
            "anonize2/relic/src/fpx/relic_fp12_mul.c",
            "anonize2/relic/src/fpx/relic_fp12_sqr.c",
            "anonize2/relic/src/fpx/relic_fp18_mul.c",
            "anonize2/relic/src/fpx/relic_fp18_sqr.c",
            "anonize2/relic/src/fpx/relic_fp2_mul.c",
            "anonize2/relic/src/fpx/relic_fp2_sqr.c",
            "anonize2/relic/src/fpx/relic_fp3_mul.c",
            "anonize2/relic/src/fpx/relic_fp3_sqr.c",
            "anonize2/relic/src/fpx/relic_fp6_mul.c",
            "anonize2/relic/src/fpx/relic_fp6_sqr.c",
            "anonize2/relic/src/fpx/relic_fpx_add.c",
            "anonize2/relic/src/fpx/relic_fpx_cmp.c",
            "anonize2/relic/src/fpx/relic_fpx_exp.c",
            "anonize2/relic/src/fpx/relic_fpx_frb.c",
            "anonize2/relic/src/fpx/relic_fpx_inv.c",
            "anonize2/relic/src/fpx/relic_fpx_pck.c",
            "anonize2/relic/src/fpx/relic_fpx_rdc.c",
            "anonize2/relic/src/fpx/relic_fpx_srt.c",
            "anonize2/relic/src/fpx/relic_fpx_util.c",
            "anonize2/relic/src/ep/relic_ep_add.c",
            "anonize2/relic/src/ep/relic_ep_curve.c",
            "anonize2/relic/src/ep/relic_ep_dbl.c",
            "anonize2/relic/src/ep/relic_ep_map.c",
            "anonize2/relic/src/ep/relic_ep_mul.c",
            "anonize2/relic/src/ep/relic_ep_mul_fix.c",
            "anonize2/relic/src/ep/relic_ep_mul_sim.c",
            "anonize2/relic/src/ep/relic_ep_neg.c",
            "anonize2/relic/src/ep/relic_ep_norm.c",
            "anonize2/relic/src/ep/relic_ep_param.c",
            "anonize2/relic/src/ep/relic_ep_pck.c",
            "anonize2/relic/src/ep/relic_ep_util.c",
            "anonize2/relic/src/epx/relic_ep2_add.c",
            "anonize2/relic/src/epx/relic_ep2_curve.c",
            "anonize2/relic/src/epx/relic_ep2_dbl.c",
            "anonize2/relic/src/epx/relic_ep2_frb.c",
            "anonize2/relic/src/epx/relic_ep2_map.c",
            "anonize2/relic/src/epx/relic_ep2_mul.c",
            "anonize2/relic/src/epx/relic_ep2_mul_fix.c",
            "anonize2/relic/src/epx/relic_ep2_mul_sim.c",
            "anonize2/relic/src/epx/relic_ep2_neg.c",
            "anonize2/relic/src/epx/relic_ep2_norm.c",
            "anonize2/relic/src/epx/relic_ep2_pck.c",
            "anonize2/relic/src/epx/relic_ep2_util.c",
            "anonize2/relic/src/pp/relic_pp_add.c",
            "anonize2/relic/src/pp/relic_pp_dbl.c",
            "anonize2/relic/src/pp/relic_pp_exp.c",
            "anonize2/relic/src/pp/relic_pp_map.c",
            "anonize2/relic/src/pp/relic_pp_norm.c",
            "anonize2/relic/src/md/blake2s-ref.c",
            "anonize2/relic/src/md/relic_md_blake2s.c",
            "anonize2/relic/src/md/relic_md_hmac.c",
            "anonize2/relic/src/md/relic_md_kdf.c",
            "anonize2/relic/src/md/relic_md_mgf.c",
            "anonize2/relic/src/md/relic_md_sha1.c",
            "anonize2/relic/src/md/relic_md_sha224.c",
            "anonize2/relic/src/md/relic_md_sha256.c",
            "anonize2/relic/src/md/relic_md_sha384.c",
            "anonize2/relic/src/md/relic_md_sha512.c",
            "anonize2/relic/src/md/sha1.c",
            "anonize2/relic/src/md/sha224-256.c",
            "anonize2/relic/src/md/sha384-512.c",
            "anonize2/relic/src/low/easy/relic_bn_add_low.c",
            "anonize2/relic/src/low/easy/relic_bn_cmp_low.c",
            "anonize2/relic/src/low/easy/relic_bn_div_low.c",
            "anonize2/relic/src/low/easy/relic_bn_mod_low.c",
            "anonize2/relic/src/low/easy/relic_bn_mul_low.c",
            "anonize2/relic/src/low/easy/relic_bn_shift_low.c",
            "anonize2/relic/src/low/easy/relic_bn_sqr_low.c",
            "anonize2/relic/src/low/easy/relic_fp_add_low.c",
            "anonize2/relic/src/low/easy/relic_fp_cmp_low.c",
            "anonize2/relic/src/low/easy/relic_fp_inv_low.c",
            "anonize2/relic/src/low/easy/relic_fp_mul_low.c",
            "anonize2/relic/src/low/easy/relic_fp_rdc_low.c",
            "anonize2/relic/src/low/easy/relic_fp_shift_low.c",
            "anonize2/relic/src/low/easy/relic_fp_sqr_low.c",
            "anonize2/relic/src/low/easy/relic_fpx_add_low.c",
            "anonize2/relic/src/low/easy/relic_fpx_mul_low.c",
            "anonize2/relic/src/low/easy/relic_fpx_rdc_low.c",
            "anonize2/relic/src/low/easy/relic_fpx_sqr_low.c",
           ],

          "xcode_settings":
            {
              "OTHER_CPLUSPLUSFLAGS" : [
                "-std=c++11",
                "-stdlib=libc++",
                "-g",
                "-O1",
                "-fomit-frame-pointer",
                "-msse2",
                "-mfpmath=sse",
                "-march=native"
              ],
              "MACOSX_DEPLOYMENT_TARGET": "10.11",
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
            }
        }]

      ],
    }
  ]
}
