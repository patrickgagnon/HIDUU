from subprocess import check_call
from settings import *


def upload_unvetted_file_unix(upload_sync = 'uploadUnvettedFile', 
                              upload_sync_id = UNVETTED_SYNC_ID,
                              system_secret = None, 
                              file_path = None, reason = None, 
                              release_date = None, sv = None,
                              file_type_id = None, 
                              data_source_id = None, 
                              source_id = None):
    command = ["{hiduu_path}hi-data-upload-utility".format(hiduu_path=HIDUU_PATH),
               "{upload_sync}".format(upload_sync=upload_sync), "-said", source_id, "-f", file_path, "-sas",
               system_secret, "-re", reason, "-sid", upload_sync_id]

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
                             upload_sync_id = VERTICA_SYNC_ID, 
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
                               upload_sync_id = VETTED_SYNC_ID, 
                               file_name = None, 
                               file_path = None, 
                               reason = None):
    command = "{hiduu_path}hi-data-upload-utility".format(
      hiduu_path=HIDUU_PATH) + upload_sync + "-said" + source_id + "-sas" + system_secret + "-sid" +
               upload_sync_id + "-rn" + file_name + "-f" + file_path, "-re" + reason

    os.system(command)




def upload_unvetted_file_win(upload_sync = 'uploadUnvettedFile', 
                              upload_sync_id = UNVETTED_SYNC_ID,
                              system_secret = None, 
                              file_path = None, reason = None, 
                              release_date = None, sv = None,
                              file_type_id = None, 
                              data_source_id = None, 
                              source_id = None):
    command = "{hiduu_path}hi-data-upload-utility".format(
      hiduu_path=HIDUU_PATH) + upload_sync + "-said" + source_id + "-f" + file_path + "-sas" + system_secret + 
    "-re" + reason + "-sid"+ upload_sync_id
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
        hiduu_path=HIDUU_PATH) + upload_sync + " -said " + source_id + " -sas " + system_secret + " -sid " + 
    upload_sync_id + " -f " + file_path + " -rl " + release_date + " -sv " + sv + " -fid " + file_type_id + " -dsid " + data_source_id
    os.system(command)

