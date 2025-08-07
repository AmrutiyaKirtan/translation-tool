from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()  # Load environment variables from .env file

class Translator:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def translate(self, text, source_lang, target_lang):
        print(f"Translating from {source_lang} to {target_lang}: {text}")  # Debug log
        source_lang = "the source language" if source_lang == "auto" else f"'{source_lang}'"
        
        # For languages that use non-Latin scripts, request romanization
        needs_romanization = target_lang in ['ja', 'zh', 'zh-TW', 'ko', 'th', 'ru', 'ar', 'hi', 'el', 'he', 'uk']
        
        if needs_romanization:
            prompt = f"""Translate this text from {source_lang} to '{target_lang}'. 
                     Return only the translation followed by its romanization in parentheses.
                     Format: "translation (romanization)"
                     Text: {text}"""
        else:
            prompt = f"Translate this text from {source_lang} to '{target_lang}'. Text: {text}"
            
        try:
            response = self.model.generate_content(prompt)
            translated_text = response.text.strip()
            
            # Clean up the response if needed
            if '(' in translated_text and ')' in translated_text:
                # Response already has romanization, return as is
                print(f"Translation result: {translated_text}")
                return translated_text
            elif needs_romanization:
                # If romanization was requested but not properly formatted, request it separately
                romanization_prompt = f"Provide only the romanization (reading) of this {target_lang} text: {translated_text}"
                try:
                    romanization_response = self.model.generate_content(romanization_prompt)
                    romanization = romanization_response.text.strip()
                    final_text = f"{translated_text} ({romanization})"
                    print(f"Translation result: {final_text}")
                    return final_text
                except:
                    return translated_text
            else:
                print(f"Translation result: {translated_text}")
                return translated_text
                
        except Exception as e:
            print(f"Translation error: {str(e)}")  # Debug log
            return f"Translation error: {str(e)}"