import azure.cognitiveservices.speech as speechsdk

def check_pronunciation(word, audio_path):
    speech_key = "YOUR_AZURE_KEY"
    region = "YOUR_REGION"

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)
    audio_config = speechsdk.audio.AudioConfig(filename=audio_path)

    config = speechsdk.PronunciationAssessmentConfig(
        reference_text=word,
        grading_system=speechsdk.PronunciationAssessmentGradingSystem.HundredMark,
        granularity=speechsdk.PronunciationAssessmentGranularity.Phoneme,
        enable_miscue=True
    )

    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    config.apply_to(recognizer)
    result = recognizer.recognize_once()
    return speechsdk.PronunciationAssessmentResult(result).pronunciation_score
