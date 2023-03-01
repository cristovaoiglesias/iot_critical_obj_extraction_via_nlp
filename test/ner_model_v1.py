# Import and load the spacy model
import spacy
from spacy.gold import GoldParse
from spacy.scorer import Scorer
import device_dt
import service_dt
import resource_dt
import random

nlp=spacy.load("en_core_web_sm")
ner=nlp.get_pipe('ner')

LABEL1 = "Device"
LABEL2 = "Resource"
LABEL3 = "Service"

TRAIN_DATA_device_dt=device_dt.dataset()
TRAIN_DATA_resource_dt=resource_dt.dataset()
TRAIN_DATA_service_dt=service_dt.dataset()

#Device dataset process
random.shuffle(TRAIN_DATA_device_dt)
random.shuffle(TRAIN_DATA_device_dt)
size_test_device_dt=round(len(TRAIN_DATA_device_dt)*0.35)
TEST_DATA_device_dt=[]
for i in TRAIN_DATA_device_dt[:size_test_device_dt]:
    sentence=i[0]
    enty=i[1]['entities']
    TEST_DATA_device_dt.append((sentence,enty))
    # print((sentence,enty))

#Resource dataset process
random.shuffle(TRAIN_DATA_resource_dt)
random.shuffle(TRAIN_DATA_resource_dt)
size_test_resource_dt=round(len(TRAIN_DATA_resource_dt)*0.35)
TEST_DATA_resource_dt=[]
for i in TRAIN_DATA_resource_dt[:size_test_resource_dt]:
    sentence=i[0]
    enty=i[1]['entities']
    TEST_DATA_resource_dt.append((sentence,enty))
    # print((sentence,enty))

#Service dataset process
random.shuffle(TRAIN_DATA_service_dt)
random.shuffle(TRAIN_DATA_service_dt)
size_test_service_dt=round(len(TRAIN_DATA_service_dt)*0.35)
TEST_DATA_service_dt=[]
for i in TRAIN_DATA_service_dt[:size_test_service_dt]:
    sentence=i[0]
    enty=i[1]['entities']
    TEST_DATA_service_dt.append((sentence,enty))
    # print((sentence,enty))




TRAIN_DATA = TRAIN_DATA_service_dt[size_test_service_dt:]+TRAIN_DATA_resource_dt[size_test_resource_dt:]+TRAIN_DATA_device_dt[size_test_device_dt:]
random.shuffle(TRAIN_DATA)
random.shuffle(TRAIN_DATA)
TEST_DATA = TEST_DATA_service_dt+TEST_DATA_resource_dt+ TEST_DATA_device_dt
random.shuffle(TEST_DATA)
random.shuffle(TEST_DATA)

text_test="""TEST_DATA=[("In addition, almost all come with a laser sensor, which picks up emissions from a laser gun as used in portable traps.", {"entities": [(36, 48, "Device")]}), ("The sensor could be inserted into tissue, excited with a laser pointer, and provide real-time, continuous monitoring of blood glucose level.", {"entities": [(4, 10, "Device")]}), ("The temperature of the water bath is controlled by a microprocessor and a temperature sensor.", {"entities": [(74, 92, "Device")]}), ("The sensor can time this journey down to the nanosecond, ESA says, meaning that the instrument is accurate to within two centimetres.", {"entities": [(4, 10, "Device")]}), ("In addition, a cheap sensor cannot distinguish between a water pipe, a structural beam and a power cable.", {"entities": [(21, 27, "Device")]}), ("These systems use radar as the surveillance and cueing sensor to achieve this.", {"entities": [(55, 61, "Device")]}), ("Microwave sensor data, thermal and radiometric information etc. can be got even under adverse weather conditions or cloud cover.", {"entities": [(0, 16, "Device")]}), ("The screen also has both a variable brightness control as well as an ambient light sensor that automatically adjusts to the environment.", {"entities": [(69, 89, "Device")]}), ("The oxygen sensor was inserted through the bark side in the same way as for the trees in the arboretum.", {"entities": [(4, 17, "Device")]}), ("Other options include 6-disc in-dash CD autochanger, sunroof and parking distance sensor.", {"entities": [(73, 88, "Device")]}), ("In tall canopies, the operator moves beneath the canopy along a linear path, keeping the sensor oriented to the sun with the help of a sight.", {"entities": [(89, 95, "Device")]}), ("The optical sensor functions as a rangefinder, measuring the height of the target beneath the missile and profiling the target simultaneously.", {"entities": [(12, 18, "Device")]}), ("The wireless sensor technology is used to monitor pressure within an aortic aneurysm.", {"entities": [(13, 19, "Device")]}), ("The sculpture is embedded with 3,000 toy dogs whose little synchronized yaps are triggered by a hidden motion sensor.", {"entities": [(103, 116, "Device")]}), ("Optimal sensor placement is desirable to ensure adequate coverage of the network's flow for detection and remediation of contaminants.", {"entities": [(8, 14, "Device")]}), ("The concept of the device is to activate a remote sensor that will trigger the device on the vehicle that will bring it to a stop.", {"entities": [(50, 56, "Device")]}), ("A small sensor, the accelerometer, placed nearby then detects the sound waves and analyses their acoustic signature.", {"entities": [(8, 14, "Device")]}), ("The breaker trips when the sensor determines that the amperage at the hot terminal is not equal to the amperage at the neutral terminal.", {"entities": [(27, 33, "Device")]}), ("We were communicating fairly well and I was about to renew my questions as to how he came to be here when the sensor alert sounded.", {"entities": [(110, 116, "Device")]}), ("In late 2009 Borkholder wrote a white paper proposal to DARPA that pitched a disposable blast gauge using a tiny pressure sensor.", {"entities": [(113, 128, "Device")]}), ("When said light enters your bloodstream only a portion is reflected and returned to the sensor thus giving you your readout.", {"entities": [(88, 94, "Device")]}), ("I told her several days ago I thought the yardmen damaged the backyard rain sensor when they trimmed the shrubs but God forbid we should listen to Rana.", {"entities": [(71, 82, "Device")]}), ("On many projects, said O'Mahony, the engineering team is left trying to fight science by being asked to achieve some unrealistic sensor or actuator accuracies.", {"entities": [(129, 135, "Device")]}), ("If a given tackle exceeds a certain level of force, the sensor is activated and the player is notified to seek medical attention.", {"entities": [(56, 62, "Device")]}),("If that actuator starts to move unexpectedly, it acts as a generator and the short provides an electrical load that slows the motor down.", {"entities": [(8, 16, "Device")]}), ("The actuator valve assembly and suction tube is screwed onto the cylinder and the tank is pressurized with a standard tire inflation system.", {"entities": [(4, 12, "Device")]}), ("The actuator is then de-energized and the switching contacts return to their starting positions.", {"entities": [(4, 12, "Device")]}), ("Each unit consisted of a quadrant and bellcrank assembly, a control valve, an actuator cylinder assembly and a bypass control assembly.", {"entities": [(78, 104, "Device")]}), ("An attachable implement such as a loader bucket is attached to the actuator.", {"entities": [(67, 75, "Device")]}), ("The Army conducted extensive testing of the trailer, with a modified brake actuator mechanism and strengthened trailer chassis and tow bar.", {"entities": [(69, 83, "Device")]}), ("The ball valve can be operated automatically through an actuator or manually with the handle.", {"entities": [(56, 64, "Device")]}), ("The actuator body pivots about a pivot axis and is attached to the cartridge bearing assembly disposed within an inner hollow of the actuator body.", {"entities": [(4, 12, "Device")]}), ("On many projects, said O'Mahony, the engineering team is left trying to fight science by being asked to achieve some unrealistic sensor or actuator accuracies.", {"entities": [(139, 147, "Device")]}), ("The voice coil actuator is not only far more adaptable and insensitive to thermal issues.", {"entities": [(4, 23, "Device")]}), ("There was no indication of any structural damage that would degrade the stiffness of the actuator attachment.", {"entities": [(89, 108, "Device")]}), ("Readjust end position OPEN according to the operation instructions of the actuator.", {"entities": [(74, 82, "Device")]}), ("The adjusting lever or actuator is fitted on the same side as the gear wheel.", {"entities": [(23, 31, "Device")]}), ("A stop valve having a thermal or motorised actuator, which varies the amount of flow as a function of ambient temperature, is suitable for this.", {"entities": [(22, 51, "Device")]}), ("The actuator also includes an electrode fabricated on the supporting substrate.", {"entities": [(4, 12, "Device")]}), ("Each of the four servos includes a hydraulic actuator and a hydraulic distributor.", {"entities": [(35, 53, "Device")]}), ("The systematic variation in the actuator parameters made it possible to enhance their performance considerably.", {"entities": [(32, 40, "Device")]}), ("The air pressure on each side of the actuator piston determines the setting of the transmission.", {"entities": [(37, 52, "Device")]}), ("The distance shall be decreased by 15 cm in the case of no ignition at 60 cm distance between burner flame and aerosol actuator.", {"entities": [(111, 127, "Device")]}), ("A piston rod of the hydraulic actuator imparts movement to a generally vertically oriented articulated linkage member.", {"entities": [(20, 38, "Device")]}), ("He struggled with his vulcanized suit, trying to squeeze from under the actuator.", {"entities": [(72, 80, "Device")]}), ("Obviously, the actuator had smashed his transmitter, but left the receiver section intact.", {"entities": [(15, 23, "Device")]}), ("The tape moved on unperturbedly, reminding him to inspect the actuator bearings and extension rods.", {"entities": [(62, 70, "Device")]})]
"""



# Add the new label to ner
ner.add_label(LABEL1)
ner.add_label(LABEL2)
ner.add_label(LABEL3)

# Resume training
optimizer = nlp.resume_training()
move_names = list(ner.move_names)

# List of pipes you want to train
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]

# List of pipes which should remain unaffected in training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]


# Importing requirements
from spacy.util import minibatch, compounding

losses2plot=[]
e2plot=[]
losses = {}

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# Begin training by disabling other pipeline components
with nlp.disable_pipes(*other_pipes) :

  sizes = compounding(1.0, 100.0, 1.001)
  # Training for 30 iterations
  for itn in range(1000):
    # shuffle examples before training
    # print("interation",itn)
    # print("Losses",losses)

    # print("Losses",losses)

    random.shuffle(TRAIN_DATA)
    # batch up the examples using spaCy's minibatch
    batches = minibatch(TRAIN_DATA, size=sizes)
    # ictionary to store losses
    losses = {}
    for batch in batches:
      texts, annotations = zip(*batch)
      # Calling update() over the iteration
      nlp.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)
      #print("Losses", losses)
    print('epoch',itn,losses["ner"])
    losses2plot.append(losses["ner"])
    e2plot.append(itn)

def evaluate(ner_model, examples):
    scorer = Scorer()
    for input_, annot in examples:
        doc_gold_text = ner_model.make_doc(input_)
        gold = GoldParse(doc_gold_text, entities=annot)
        pred_value = ner_model(input_)
        scorer.score(pred_value, gold)
    return scorer.scores


doc = nlp(text_test)
print("\n\n\Test data\n\n")
for ent in doc.ents:
  print(ent.text,ent.label_)

print("n\n\ Precision (p), Recall(r) and F-score(f) \n\n")
results = evaluate(nlp, TEST_DATA)
print(results['ents_per_type'])

import matplotlib.pyplot as plt



current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
