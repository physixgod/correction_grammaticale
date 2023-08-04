from language_tool_python import LanguageTool
def correct(text,language):
    language_used= LanguageTool(language)
    corrected_text = language_used.correct(text)
    print(f"Text before change: {text}")
    print(f"Text after change: {corrected_text}")
    return corrected_text
text_to_correct = "Je mapele Mostfa , je suis 23 ans et j ai un etudiant en genie inforrmatique"
L="fr"
correct(text_to_correct,L)
