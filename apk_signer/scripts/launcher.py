import click
from subprocess import check_output

from apk_signer import config
from apk_signer.apksigner import launcher 
from androguard.core.bytecodes.apk import APK

@click.command()
@click.option('--run', is_flag=True)
@click.option('--default', is_flag=True)
@click.option('--ks_pass', default='pyapksigner123!')
@click.option('--key_pass', default='pyapksigner123!')
@click.option('--key_alias', default='pyapksigner')
@click.option('--key_path', default='pyapksigner.jks')
@click.argument('apk')
def cli(apk: str, default: bool, key_path: str, key_alias: str, key_pass: str, ks_pass: str, run: bool):
    if key_path == 'pyapksigner.jks':
        if not default:
            print("[Warning] Signing with default keystore.")
            print("[Warning] Please pass --key_path, --key_alias, --key_pass, --ks_pass parameter, if you want to use your keystore")
        key_path = str(config.ROOT_DIR.joinpath(key_path).resolve())

    apk_path = launcher(apk, key_path, key_alias, key_pass, ks_pass)

    if run:
       apk = APK(apk_path) 

       def adb(cmd):
           try:
               r = check_output('adb {}'.format(cmd), shell=True) 
               return r
           except:
               return
           
       print(adb('uninstall %s' % apk.package))
       print(adb('install "%s"' % apk_path))
       print(adb('shell am start -n %s/%s' % (apk.package, apk.get_main_activity())))

    return

if __name__=="__main__":
    cli()
