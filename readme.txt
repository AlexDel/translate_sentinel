This module performs evaluation of sense-distortion in translation.
Original text and its translation are analyzed under several parameters and decision about vandalism is made.

1. Module structure
    Module is run with main.py.

    main.py API:
        process() - takes json-input and returns boolean whether the translation is vandal or not
        debug() - takes json-input and returns values of evaluated parameteres


    Here is an example usage of Translate sentinel module:

        >>> from translate_sentinel import main
        >>> print main.process(translation_object)
         ...False
        >>> print main.debug(translation_object)
         ...False
            String_target_length  218
            Length_difference  0.703196347032
            Digits_amount  0.00456621004566
            Digits_blocks_intersection  0.0
            Target_upper_case  1.0
            Longest_symbol_repetition  0
            Longest_word  15
            BLEU_metrics  0.666666666667
            Bigram_calculator  0.0
            Levenstein_calculator  0.333333333333
            Braun_Balke_calculator  0.666666666667
            Profanity_calculator  1.0
            Semantic_calculator  0.318931803491

2. Input structure and requirements
   Functions process() and debug() takes json-strings as inputs and return json as well
   Structure of the the inpu json is the following:

        {
        "orig": {
            "lang": "en",
            "text": "Are your foregrounds fighting for the users’ attention?"
            },
        "target": {
            "lang": "ru",
             "text": "Объекты вашего переднего плана борются за внимание пользователей?"
             }
        }
   NB! Special symbols in json like ; " : { and { should be escaped in "text" values.

All bugs and issues are welcome at https://bitbucket.org/AlexDel/translate_sentinel/