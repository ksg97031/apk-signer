apk-signer
============================================================
| apk-signer can sign the apk file.

.. code:: sh

  $ pip install apk-signer
  $ apk-signer {APK_PATH} --default
  > {SIGNED_APK_PATH}
  $ apk-signer {APK_PATH} 
  > [Warning] Signing with default keystore.
  > [Warning] Please pass --key_path, --key_alias, --key_pass, --ks_pass parameter, if you want to use your keystore
  > {SIGNED_APK_PATH}
  $ apk-signer --key_path="sample.jks" --key_alias="sample" --key_pass="sample_key" --ks_pass="sample_ks"
  > {SIGNED_APK_PATH}


