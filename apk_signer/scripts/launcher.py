import click
from apk_signer import config
from apk_signer.apksigner import launcher 

@click.command()
@click.option('--default', is_flag=True)
@click.option('--ks_pass', default='pyapksigner123!')
@click.option('--key_pass', default='pyapksigner123!')
@click.option('--key_alias', default='pyapksigner')
@click.option('--key_path', default='pyapksigner.jks')
@click.argument('apk')
def cli(apk: str, default: bool, key_path: str, key_alias: str, key_pass: str, ks_pass: str):
    if key_path == 'pyapksigner.jks':
        if not default:
            print("[Warning] Signing with default keystore.")
            print("[Warning] Please pass --key_path, --key_alias, --key_pass, --ks_pass parameter, if you want to use your keystore")
        key_path = str(config.ROOT_DIR.joinpath(key_path).resolve())

    launcher(apk, key_path, key_alias, key_pass, ks_pass)
    return

if __name__=="__main__":
    cli()
