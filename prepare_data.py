import os
#import glob
import csv
import shutil
import pickle
import json
import wave

target_dir = 'assets/wavs'
source_dir = '/DATA/nina/CommonPhone/CP'


def read_train_and_dev_csv_files(path, speakers_audiofiles):
    first = True
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if first:
                # skip first line
                first = False
                continue
            if row[1] not in speakers_audiofiles.keys():
                speakers_audiofiles[row[1]] = []
            speakers_audiofiles[row[1]].append(row[0].replace('mp3', 'wav'))


# remove directories and create them so that they are empty
#path_train = os.path.join(target_dir, 'train')
#path_test = os.path.join(target_dir, 'test')
#dir_list = os.listdir(target_dir)
#if 'train' in dir_list:
#    shutil.rmtree(path_train)
'''if 'test' in dir_list:
    shutil.rmtree(path_test)'''
#dir_list = os.listdir(target_dir)
#if 'train' not in dir_list:
#    os.mkdir(path_train)
'''if 'test' not in dir_list:
    os.mkdir(path_test)'''
shutil.rmtree(target_dir)
os.mkdir(target_dir)

# remove_files_from_directory(path_train)
# remove_files_from_directory(path_test)

# id-counter, gives speakers an integer value
id_ctr = 0
#id_ctr_val = 8401
#metadata dict
speakers = {}
#speakers_val = {}

# go through all language subfolders of target directory and extract files to source directory
for lang in ['en']:#os.listdir(source_dir):
    path_lang_subfolder = os.path.join(source_dir, lang)

    # read train.csv and dev.csv and create a dictionary that assigns ids to audio file names
    speakers_audiofiles = {}
    path = os.path.join(path_lang_subfolder, 'train.csv')
    read_train_and_dev_csv_files(path, speakers_audiofiles)
    path = os.path.join(path_lang_subfolder, 'dev.csv')
    read_train_and_dev_csv_files(path, speakers_audiofiles)

    # read meta.csv file, and for each speaker, create a new folder in the right directory, copy the corresponding .wav files and add metadata to spk_meta.pkl
    first = True
    path = os.path.join(path_lang_subfolder, 'meta.csv')
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if first:
                # skip first line
                first = False
                continue
            # 0: id, 1: gender, 2: age, 3: locale, 4: accent, 5: set
            if row[0] in ["6e114681569d8d40538452f28f28c70f9a16a9b1a5b9a11252cf4faf35947fd1a7697c308ccfda862ea8487bd3be5420f1d9438c4570e0617d1b9f654b49efb3", "5f9e4c2e14df2e6c22b6c8a0c9c5a69358a359fbba2490e686d712972ac25cb19af740f187a138b4340e2b6f8b0f6bd5fd53fd4335cd09f9ba8e9aae433362ba", "88db75b2bb20266c61abddf381931454807443bc745635dac0b61158cd39f5765327ed5dbba83a7bc57decd4df12d27ce194149e10459b80276a2898785dfaea", "990418b33c7fbe3ae624392e19699c60a7c124cbc24a2c46a893f9148a4292eba2282308d371506a539e6819aee816398aaac1b1b79890f1cacb86f2b1e979bc", "6828466dbd26de0108062d98c003551714f82675c17a67c0fb6ab6a071c17210e6de152cadb2b8390b513ded82b7f0d63a269e564ab6be475b4445f003c31b9c", "d0498a01e09fe558bed38f49ab41a04a97100d91ddb4a7415fb4ea2915e331a478facdd0a48df54b5cc6aa16d51ef1f5fc2850ecd9dcd52c0bad23b684ae0f90", "358cf8fa2c9a22ee87a8ec9ee8bb0150bdc56f813656899f5cb8851fbed3f20bddb838879ca29bec69ccb72f50b87f8acbe66e7698cabfbb939d9b4168944b5f", "08930728bedf2893e48e6454117b456857cdf6eb08e0043cbf36f00023ff168a1eef8458c54286d0fcf58f103ce87a46377a2b41d8267ba6d388f3f54600f505", "a6cc1ca2490da26fe568cb3e427856cdb10e6fe4e3843f43967128c95b3b359906257ece77e1dea7d1e08cff6ae27641babc682ef9f392f5ac9882b093da8d64", "84e7b74a19834676fd6248f0f18adb0eeeee7312e8c129164dbaf9984ffa9f86e0b91988d6cb196fd92f57788bbbf2ec6c6076082991d6a662b598600a8d9fd4", "7c81165b737418da848e66287d5e267bde4ef88085ff158b25cfc8e1f5e798e808f89a0929636b46d191292dbf137332d53abe190d321e1a2e85ffc7018d8442", "5c33f714722de22324b1b6957075416253feba7a43f865af139fd11912737ce5b7d826e93ced3301cecfbf3df95762afb4d2be3bf931602fbcecef3c0b305145", "3dfdcc88d6d57d1530f38a702f19c78e826b293f7b46b7c41599dee8252347294177ab56aab4e57dd7d5b873b8dc93ccadb667395aa921bb12541af62fbece73", "7311664fe59284d22c369371a95747f5acf6fc6708e6edf40c0865c77c7bd92577a1302240acc4882fbb913bb1a4060e34a358bc06631761e69d8c119877d765", "68b7da78dba896ca587887e3a2f73ff4d799400e0cb86d127740895884e89103f35d8a6b5ab1dfccf8ab90c155126d5a235e8fafad376beb7e182c38ef71c377", "b57f832fdc88417ef9bb21e191e80cce38f337c2560b8eb9a3df869f5ab4365112bbe9ceeb63551c9dfca4bf8616e06ab4c7bc856518cdb6a9a4c19867880592"]:
                continue	
            path = ""
            #if row[0] not in ["a19a6987c05a9d62247d356dbe18c581eccb78728b839bbd1491cdd60bf81651699b96d5f3732d99275684abb397c4f3b40383b3a6aaecb310accee17755623f", "6e114681569d8d40538452f28f28c70f9a16a9b1a5b9a11252cf4faf35947fd1a7697c308ccfda862ea8487bd3be5420f1d9438c4570e0617d1b9f654b49efb3"]:
            #    continue
            if row[5] == "train":
                path = os.path.join(target_dir, "P" + str(id_ctr))
            elif row[5] == "dev":
                #print(id_ctr_val)
                path = os.path.join(target_dir, "P" + str(id_ctr))
            if path != "":
                # make directory for speaker
                os.mkdir(path)
                # join all audio files for speaker in directory
                outfile = os.path.join(path, str(id_ctr) +   '.wav')
                data = []
                for audiofile in speakers_audiofiles[row[0]]:
                    #shutil.copy(os.path.join(path_lang_subfolder, 'wav', audiofile), path)
                    w = wave.open(os.path.join(path_lang_subfolder, 'wav', audiofile), 'rb')
                    data.append( [w.getparams(), w.readframes(w.getnframes())])
                    w.close()
                    #print(audiofile)
                output = wave.open(outfile, 'wb')
                output.setparams(data[0][0])
                for i in range(len(data)):
                    output.writeframes(data[i][1])
                output.close()
                #add speaker info to metadata dict
                if row[1] == "male":
                    if row[5] == "train":
                        speakers["P" + str(id_ctr)] = "M"
                        id_ctr += 1
                    else:
                        speakers["P" + str(id_ctr)] = "M"
                        id_ctr += 1
                else:
                    if row[5] == "train":
                        speakers["P" + str(id_ctr)] = "F"
                        id_ctr += 1
                    else:
                        speakers["P" + str(id_ctr)] = "F"
                        id_ctr += 1

#print("length of speaker dict: " + str(len(speakers.keys())))

#with open('validation.pkl', 'wb+') as handle:
#    pickle.dump(speakers, handle)
with open('assets/spk2gen.pkl', 'wb+') as handle:
    pickle.dump(speakers, handle)

with open('metadata.txt', 'w+') as metadata_file:
    metadata_file.write(json.dumps(speakers))

#with open('val.txt', 'w+') as val_file:
#    val_file.write(json.dumps(speakers_val))
