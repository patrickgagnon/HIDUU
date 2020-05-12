from subprocess import check_call
import os


def hiduu_upload(hiduu_path = None,
                 upload_command = None,
                 system_account_id = None,
                 system_account_secret = None,
                 source_id = None,
                 data_set_id = None,
                 file_id = None,
                 file_release = None,
                 spec_version = None,
                 file = None,
                 reason=None,
                 sub_source=None,
                 record_count= None,
                 discovery=None,
                 args=None,
                 encryption = None,
                 client_mnemonic = None):
        command = ["{hiduu_path}hi-data-upload-utility".format(hiduu_path=hiduu_path),
                   "{upload_command}".format(upload_command=upload_command),
                   "-said",system_account_id,
                   "-sas",system_account_secret,
                   "-sid",source_id]
        if upload_command == 'uploadUnvettedFile':
            command.append("-f")
            command.append(file)
            command.append("-re")
            command.append(reason)
        if upload_command == 'uploadDataSetFile':
            command.append("-dsid")
            command.append(data_set_id)
            command.append("-sv")
            command.append(spec_version)
            command.append("-fid")
            command.append(file_id)
            command.append("-rl")
            command.append(file_release)
            command.append("-f")
            command.append(file)
        if upload_command == 'uploadReferenceFile':
            command.append("-rn")
            command.append(data_set_id)
            command.append('-f')
            command.append(file)
            command.append('-re')
            command.append(reason)

        check_call(command)


def hiduu_upload_win(hiduu_path = None,
                     upload_command = None,
                     system_account_id = None,
                     system_account_secret = None,
                     source_id = None,
                     data_set_id = None,
                     file_id = None,
                     file_release = None,
                     spec_version = None,
                     file = None,
                     reason = None,
                     sub_source = None,
                     record_count = None,
                     discovery = None,
                     args = None,
                     encryption = None,
                     client_mnemonic = None):
    command = ["{hiduu_path}hi-data-upload-utility".format(hiduu_path=hiduu_path),
               "{upload_command}".format(upload_command=upload_command),
               " -said ", system_account_id,
               " -sas ", system_account_secret,
               " -sid ", source_id]
    if upload_command == 'uploadUnvettedFile':
        command +" -f " + file + " -re " + reason

    if upload_command == 'uploadDataSetFile':
        command + " -dsid " + data_set_id + " -sv " + spec_version + " -fid " + file_id + " -rl " + file_release + " -f " + file

    if upload_command == 'uploadReferenceFile':
        command + " -rn " + data_set_id + " -f " + file + " -re " + reason

    os.system(command)
