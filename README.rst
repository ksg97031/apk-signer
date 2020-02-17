apk-signer
============================================================
| Easy to use apk signing

.. code-block:: sh

   pip install apk-signer
   

.. code-block:: sh

  $ apk-signer sample.apk
  [Warning] Signing with default keystore.
  [Warning] Please pass --key_path, --key_alias, --key_pass, --ks_pass parameter, if you want to use your keystore
  > sample-signed.apk
  $ apk-signer sample.apk --key_path="sample.jks" --key_alias="sample" --key_pass="sample_key" --ks_pass="sample_ks"
  > sample-signed.apk
  $ apk-signer sample.apk --run
  > Success
  > Performing Streamed Install\nSuccess
  > Starting: Intent { cmp=com.sample.activty/.MainActivity }



