# Urdu-OCR
Our project is a Desktop based OCR software that takes an Urdu text image as input (particularly in the Naskh font),
performs extraction techniques on it and later generates recognized editable text. Urdu OCR deals with multiple input image formats namely: JPEG, JPG, PNG and BMP. 
Urdu OCR has long term benefits for the visually impaired individuals as we can use text-to-speech synthesizers to convert the OCR generated text to audio at real time.
This project was developed collaboratively by me and my two teammates.

**System Requirements** <br>
Urdu OCR makes use of the Tesseract OCR software for extraction of the hard printed text. We chose Python as our programming language, Ubuntu 18.04 as our Operating System, PyCharm as the python platform and three important python libraries for image processing and analysis, namely: Python Imaging Library, PyQt5 and OpenCV. 

**Methodology** <br>
The methodology that we have adopted for our project is training the Long Short Term Memory (LSTM) Recurrent Neural Network for our particular Urdu font i.e. Naskh. The main component in our software is the Tesseract OCR which performs the real tasks of text recognition. Tesseract 4.0 incorporates the line recognizer engine i.e. LSTM. We have used a fine tuned model, making use of the Tesseract’s inbuilt urd.traineddata file. Fine tuning is the process of training an existing model on new data without changing any part of the network.
Naskh is an important Urdu font which is written along the horizontal line which makes its training a little less complicated than other cursive fonts. 
As the first step, we build up our environment with all the compatible versions. Next we load the necessary LangData and urd files from GitHub such as the unicharset, font properties, xheights, common punctuation, urd.traineddata, numbers, wordlist, forbidden characters and font.txt files.
As the next step, we create our training dataset through the tesstrain.sh script where we have to specify our language, font i.e. ‘Nafees Naskh’, no. of pages, files directories and the file format. Next we extract our LSTM model from the existing trained data file and evaluate this model on our new font.
Afterwards, we fine tune the LSTM model on the new font ‘Naskh/Nafees’. Using the pre-trained urd.traineddata file, we add our own training data for adapting the software for our font and for more accuracy. The training process makes use of the box file created through the tesstrain script and the existing urd.traineddata file to model our neural network to recognize the new font. Training takes a considerable amount of amount so we declare checkpoints for cases where network/system connection gets disrupted, consequently, training proceeds without any data/progress loss. 

**Final Deliverable** <br>
The final deliverable of our project is a Desktop based application which first prompts the user to select an image from the device’s directory, next the user has an option to edit the selected image or directly extract the text. The user can crop a portion out of the image or rotate it by inputting the degree of rotation. Later, when the user clicks the Continue button, Tesseracts performs its tasks and returns the OCR generated text in a text box. Here the user has the option to edit the text at real time, save it in a text file or edit the text after converting it to a .txt file. 



