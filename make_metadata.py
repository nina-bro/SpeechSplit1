import os
import pickle
import numpy as np

rootDir = 'assets/spmel'
dirName, subdirList, _ = next(os.walk(rootDir))
print('Found directory: %s' % dirName)


trainSpeakers = []
valSpeakers = []
numSpeakers = 5481 #9810
#maxMelLength = 0
onehot = 0

for speaker in sorted(subdirList):
    print('Processing speaker: %s' % speaker)
    id = int(speaker.split('P')[1])
    _, _, fileList = next(os.walk(os.path.join(dirName, speaker)))
    for fileName in sorted(fileList):
        if id < 4716:
            trainUtterances = []
            trainUtterances.append(speaker)
            #spk embedding (one hot)
            spkid = np.zeros((numSpeakers,), dtype=np.float32)
            spkid[onehot] = 1.0
            trainUtterances.append(spkid)
            trainUtterances.append(os.path.join(speaker,fileName))
            trainSpeakers.append(trainUtterances)
        if id >= 4716: 
        #id >= 8401:
            #speaker (folder name)
            valStructure = []
            valStructure.append(speaker)
            #speaker-embedding (one-hot)
            spkid = np.zeros((1,numSpeakers), dtype=np.float32)
            spkid[0,onehot] = 1.0
            valStructure.append(spkid)
            valData = []
            mel = np.load(os.path.join(rootDir, speaker, fileName))
            valData.append(mel)
            #normed-f0
            raptf0Dir = 'assets/raptf0'
            raptf0 = np.load(os.path.join(raptf0Dir, speaker, fileName))
            valData.append(raptf0)
            #length
            length = mel.shape[0]
            valData.append(length)
            #filename with no file-extension
            valData.append(fileName[:-4])
            #add valData, and add to final list, which will be written to file val.pkl
            valStructure.append(valData)
            valSpeakers.append(valStructure)
            # next iteration == next speaker
    onehot += 1
        # create file list
        #for fileName in sorted(fileList):
        #    utterances.append(os.path.join(speaker,fileName))
        #    speakers.append(utterances)

print(len(trainSpeakers))
print(len(valSpeakers))
with open(os.path.join(rootDir, 'train.pkl'), 'wb') as handle:
    pickle.dump(trainSpeakers, handle)
with open(os.path.join(rootDir[:-6], 'spmel/val.pkl'), 'wb') as handle:
    pickle.dump(valSpeakers, handle)
