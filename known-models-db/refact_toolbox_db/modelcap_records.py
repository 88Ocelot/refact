from code_contrast.model_caps.modelcap_struct import ModelFunction, load_mini_html


db = [
    # ModelFunction(
    #     "select-and-refactor", 0, "Select & Refactor",
    #     supports_highlight=False,
    #     supports_selection=True,
    #     selected_lines_min=1,
    #     selected_lines_max=20,
    #     third_party=False,
    #     supports_languages="*.*",
    #     mini_html=load_mini_html("select-and-refactor"),
    #     model="CONTRASTcode",
    #     function_selection="diff-selection",
    #     catch_all_selection=True,
    # ),

    # ModelFunction(
    #     "hl-and-fix", 0, "Highlight & Fix",
    #     supports_highlight=True,
    #     supports_selection=False,
    #     selected_lines_min=0,
    #     selected_lines_max=0,
    #     third_party=False,
    #     supports_languages="*.*",
    #     mini_html=load_mini_html("hl-and-fix"),
    #     model="CONTRASTcode",
    #     function_highlight="highlight",
    #     function_hl_click="diff-atcursor",
    #     catch_all_hl=True,
    # ),

    # ModelFunction(
    #     "add-type-hints", 0, "Add Type Hints",
    #     supports_highlight=True,
    #     supports_selection=True,
    #     selected_lines_min=1,
    #     selected_lines_max=10,
    #     third_party=False,
    #     supports_languages="*.py;*.php;*.js",
    #     mini_html=load_mini_html("add-type-hints"),
    #     model="CONTRASTcode",
    #     model_fixed_intent="Add type hints",
    #     function_highlight="highlight",
    #     function_hl_click="diff-atcursor",
    #     function_selection="diff-selection",
    # ),

    ModelFunction(
        "free-chat", 1, "Chat",
        supports_highlight=True,
        supports_selection=True,
        selected_lines_min=1,
        selected_lines_max=15,
        third_party=[True, True, False],
        supports_languages="*.*",
        mini_html=load_mini_html("free-chat"),
        model=["gpt3.5", "gpt4", "starchat"],
        catch_question_mark=True,
    ),

    ModelFunction(
        "db-chat", 1, "Chat",
        supports_highlight=True,
        supports_selection=True,
        selected_lines_min=1,
        selected_lines_max=15,
        third_party=[True],
        supports_languages="*.*",
        mini_html=load_mini_html("free-chat"),
        model=["gpt3.5func"],
    ),

    ModelFunction(
        "add-console-logs", 1, "Add Console Logs",
        supports_highlight=False,
        supports_selection=True,
        selected_lines_min=1,
        selected_lines_max=20,
        third_party=[True],
        supports_languages="*.*",
        mini_html=load_mini_html("add-console-logs"),
        model=["gpt3.5"],
        model_fixed_intent="Add console logs",
    ),

    ModelFunction(
        "comment-each-line", 1, "Comment Each Line",
        supports_highlight=False,
        supports_selection=True,
        selected_lines_min=1,
        selected_lines_max=20,
        third_party=[True],
        supports_languages="*.*",
        mini_html=load_mini_html("comment-each-line"),
        model=["gpt3.5"],
        model_fixed_intent="Comment each line",
    ),

    ModelFunction(
        "explain-code-block", 1, "Explain Code",
        supports_highlight=False,
        supports_selection=True,
        selected_lines_min=1,
        selected_lines_max=30,
        third_party=[True, True],
        supports_languages="*.*",
        mini_html=load_mini_html("explain-code-block"),
        model=["gpt3.5", "gpt4"],
        model_fixed_intent="Explain Code",
    ),

    ModelFunction(
        "fix-bug", 1, "Fix Bug",
        supports_highlight=False,
        supports_selection=True,
        selected_lines_min=1,
        selected_lines_max=30,
        third_party=[True, True],
        supports_languages="*.*",
        mini_html=load_mini_html("fix-bug"),
        model=["gpt3.5", "gpt4"],
        model_fixed_intent="Fix Bug",
    ),

    ModelFunction(
        "make-code-shorter", 1, "Make Code Shorter",
        supports_highlight=False,
        supports_selection=True,
        selected_lines_min=1,
        selected_lines_max=30,
        third_party=[True, True],
        supports_languages="*.*",
        mini_html=load_mini_html("make-code-shorter"),
        model=["gpt3.5", "gpt4"],
        model_fixed_intent="Make Code Shorter",
    ),

    ModelFunction(
        "precise-naming", 1, "Precise Naming",
        supports_highlight=False,
        supports_selection=True,
        selected_lines_min=1,
        selected_lines_max=30,
        third_party=[True],
        supports_languages="*.*",
        mini_html=load_mini_html("precise-naming"),
        model=["gpt3.5"],
        model_fixed_intent="Precise Naming",
    ),

    ModelFunction(
        "completion", 1, "Completion",
        supports_highlight=False,
        supports_selection=False,
        selected_lines_min=1,
        selected_lines_max=30,
        third_party=[True, True],
        supports_languages="*.*",
        mini_html="",
        model=["gpt3.5", "gpt4"],
        model_fixed_intent="Completion",
    ),
]
