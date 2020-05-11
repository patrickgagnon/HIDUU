from subprocess import check_call
import os
from settings import *



def hiduu_upload(upload_command = None,
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
        command = ["{hiduu_path}hi-data-upload-utility".format(hiduu_path=HIDUU_PATH),
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


def upload_unvetted_file_unix(upload_sync = 'uploadUnvettedFile', 
                              upload_sync_id = None,
                              system_secret = None, 
                              file_path = None,
                              reason = None,
                              release_date = None,
                              sv = None,
                              file_type_id = None, 
                              data_source_id = None, 
                              source_id = None):
    command = ["{hiduu_path}hi-data-upload-utility".format(hiduu_path=HIDUU_PATH),
               "{upload_sync}".format(upload_sync=upload_sync),
               "-said", source_id,
               "-f", file_path,
               "-sas", system_secret,
               "-re", reason,
               "-sid", upload_sync_id]

    if upload_sync == 'uploadUnvettedFile':
        command.append("-rl") 
        command.append(release_date)
        command.append("-sv")
        command.append(sv)
        command.append("-fid")
        command.append(file_type_id)
        command.append("-dsid")
        command.append(data_source_id)

    check_call(command)





def upload_dataset_file_unix(upload_sync = 'uploadDataSetFile', 
                             upload_sync_id = None,
                             system_secret = None,
                             file_path = None, 
                             release_date = None, 
                             sv = None, 
                             file_type_id = None,
                             data_source_id = None, 
                             source_id = None):
    command = ["{hiduu_path}hi-data-upload-utility".format(hiduu_path=HIDUU_PATH),
               "{upload_sync}".format(upload_sync=upload_sync), "-said", source_id, "-sas", system_secret, "-sid",
               upload_sync_id, "-f", file_path]

    if upload_sync == 'uploadDataSetFile':
        command.append("-rl")
        command.append(release_date)
        command.append("-sv")
        command.append(sv)
        command.append("-fid")
        command.append(file_type_id)
        command.append("-dsid")
        command.append(data_source_id)
        
    check_call(command)


def upload_reference_file_win(upload_sync = 'uploadReferenceFile', 
                               source_id = None, 
                               system_secret = None,
                               upload_sync_id = None,
                               file_name = None, 
                               file_path = None, 
                               reason = None):
    command = "{hiduu_path}hi-data-upload-utility".format(
      hiduu_path=HIDUU_PATH) + upload_sync + "-said" + source_id + "-sas" + system_secret + "-sid" + upload_sync_id + "-rn" + file_name + "-f" + file_path, "-re" + reason
    os.system(command)




def upload_unvetted_file_win(upload_sync = 'uploadUnvettedFile', 
                              upload_sync_id = None,
                              system_secret = None, 
                              file_path = None, reason = None, 
                              release_date = None, sv = None,
                              file_type_id = None, 
                              data_source_id = None, 
                              source_id = None):
    command = "{hiduu_path}hi-data-upload-utility".format(
      hiduu_path=HIDUU_PATH) + upload_sync + "-said" + source_id + "-f" + file_path + "-sas" + system_secret + "-re" + reason + "-sid"+ upload_sync_id
    os.system(command)



def upload_dataset_file_win(upload_sync = 'uploadDataSetFile', 
                            upload_sync_id = None, 
                            system_secret = None,
                            file_path = None, 
                            release_date = None, 
                            sv = None, 
                            file_type_id = None,
                            data_source_id = None, 
                            source_id = None):
    command = "{hiduu_path}hi-data-upload-utility ".format(
        hiduu_path=HIDUU_PATH) + upload_sync + " -said " + source_id + " -sas " + system_secret + " -sid " + upload_sync_id + " -f " + file_path + " -rl " + release_date + " -sv " + sv + " -fid " + file_type_id + " -dsid " + data_source_id
    os.system(command)

