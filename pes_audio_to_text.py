import time
from googletrans import Translator
import speech_recognition as sr
import pathlib
import csv

def translate_from_wav_file(wav_file:str):
    """
    Returns three strings by given the wav file location or file-like-object.
    If fails, its gonna return three times the code error provided by the library

    Args:
        wav_file (str): full path location of the wav file

    Returns:
        str: first value is the original language, second value is the first translation language 
        and third value is the second translation value.
    """
    audio_file=sr.AudioFile(wav_file)
    with audio_file:
        audio = recognizer.record(audio_file)
        try:
            original = recognizer.recognize_google(audio,language=src_lang_audio)
            translated_lang1 = translator.translate(original,dest=dst_lang_txt_1,src=src_lang_txt).text
            translated_lang2 = ""
            if dst_lang_txt_2!="":
                translated_lang2 = translator.translate(original,dest=dst_lang_txt_2,src=src_lang_txt).text
            #print(original)
            #print(translated)
        except Exception as e:
            #print("Exception: "+str(e))
            return str(e), str(e), str(e)
    return original, translated_lang1, translated_lang2

def get_files_from_folder(folder:str,extension:str):
    """
    Return a String list containing the folders inside the given folder and extension with the full path

    Args:
        folder (str): Folder where we search the files
        extension (str): Filter extension

    Returns:
        List[str]: List containing the full path for the files matching the extension
    """
    return [str(p.resolve()) for p in pathlib.Path(folder).iterdir() if p.is_file() and str(p).endswith(extension)]

if __name__ == "__main__":
    src_lang_audio = "ko-KR"
    src_lang_txt = "ko"
    dst_lang_txt_1 = "en"
    dst_lang_txt_2 = "es"
    wav_files_folder = "test_files/k_sound"

    translator = Translator()
    recognizer = sr.Recognizer()
    wav_in_folder =get_files_from_folder(wav_files_folder,".wav")
    total_wav_files = len(wav_in_folder)

    start_time = time.time()
    with open("translated k_sound.csv","w",encoding="utf-8",newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',quoting=csv.QUOTE_ALL,quotechar="\"")
        writer.writerow(["ADX File", "Korean", "English", "Spanish"])
        for i in range(total_wav_files):
            resp = (translate_from_wav_file(wav_in_folder[i]))
            #print(str(pathlib.Path(wav_in_folder[i]).stem) + ", " + resp[0] + ", " + resp[1] + ", " + resp[2] + "\n")
            writer.writerow([(str(pathlib.Path(wav_in_folder[i]).stem))] + list(resp))
    print("--- %s seconds ---" % (time.time() - start_time))