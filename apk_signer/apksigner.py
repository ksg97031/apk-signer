import sys
from zipfile import ZipFile
from pathlib import Path
from subprocess import check_output
from apk_signer import config


def remove_meta_inf(p_apk):
    if isinstance(p_apk, str):
        raise Exception("p_apk is not str type")

    zip = ZipFile(p_apk)
    for l in zip.namelist():
        if l.startswith('META-INF/'):
            is_signed = True
            break
    else:
        is_signed = False

    if is_signed:
        unsinged_apk_path = str(p_apk.resolve())[:-4] + "-unsigned.apk"
        zout = ZipFile(unsinged_apk_path, 'w')
        for item in zip.infolist():
            buffer = zip.read(item.filename)
            if not item.filename.startswith('META-INF/'):
                zout.writestr(item, buffer)
        zout.close()
        zip.close()
        return Path(unsinged_apk_path)
                
    return p_apk

def apksign(p_apk, key_path: str, key_alias: str, key_pass: str, ks_pass: str):
    try:
        signed_apk_name = p_apk.name.replace("-zipaligned.apk", "-signed.apk")
        psigned_apk = p_apk.parent.joinpath(signed_apk_name)

        key_cmd = ['--ks', key_path, '--ks-key-alias', key_alias, '--ks-pass', 'pass:{}'.format(ks_pass), '--key-pass', 'pass:{}'.format(key_pass)]
        cmd = [config.apksigner, 'sign'] + key_cmd + ['--out', str(psigned_apk.resolve()), str(p_apk.resolve())]
        r = check_output(cmd)
    except Exception as e:
        print("apk signing error: " + str(e))
        return False

    return psigned_apk 

def zipalign(p_apk):
    try:
        zipaligned_apk_name = p_apk.name.replace("-unsigned.apk", "")
        if zipaligned_apk_name.endswith(".apk"):
            zipaligned_apk_name = zipaligned_apk_name[:-4]
        
        zipaligned_apk_name = zipaligned_apk_name + "-zipaligned.apk"
        p_zipaligned_apk = p_apk.parent.joinpath(zipaligned_apk_name)
        if p_zipaligned_apk.exists():
            p_zipaligned_apk.unlink()

        cmd = [config.zipalign, '-v', '-p', '4', str(p_apk.resolve()), str(p_zipaligned_apk.resolve())]
        r = check_output(cmd)
    except Exception as e:
        print("apk zipalign error: " + str(e))
        return False

    return p_zipaligned_apk

def launcher(apk: str, key_path: str, key_alias: str, key_pass: str, ks_pass: str):
    p_apk = Path(apk)
    if not p_apk.exists():
        raise Exception("File not founded: " + str(p_apk.resolve()))

    p_unsigned_apk = remove_meta_inf(p_apk)
    p_zipaligned_apk = zipalign(p_unsigned_apk)
    if p_zipaligned_apk:
        p_unsigned_apk.unlink()
        p_signed_apk = apksign(p_zipaligned_apk, key_path, key_alias, key_pass, ks_pass)
        if p_signed_apk:
            p_zipaligned_apk.unlink()
            apk = str(p_signed_apk.resolve())
            print(apk)
            return apk
