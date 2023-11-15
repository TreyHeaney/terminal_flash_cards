class PromptStrings:
    press_enter = 'Press ENTER to continue.'
    def mm_choices(signed_in):
        return f'''a: View card groups
b: Manage Save
c: Settings
d: {'Sign in or sign up' if not signed_in else 'Sign out'}'''
    
    class cards:
        get_question = 'What is the question for this card?\n'
        get_answer = 'What is the answer for this card?\n'
        faux_answer = 'What are some faux answers for this card? (ENTER to stop)\n'
        update_question = 'Enter updated card question (ENTER to skip, X to delete)'
