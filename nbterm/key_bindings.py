from prompt_toolkit.filters import Condition

DEFAULT_KEY_BINDINGS = {
    "exit": "c-q",
    "save": "c-s",
    "enter_cell_to_edit": "enter",
    "exit_cell_to_command": "escape",
    "go_up": "up",
    "go_down": "down",
    "move_cell_up": "c-up",
    "move_cell_down": "c-down",
    "clear_output": "l",
    "make_cell_markdown": "m",
    "make_cell_code": "o",
    "run_cell_and_stay": "c-e",
    "run_cell_and_select_below": "c-r",
    "cut_cell": "x",
    "copy_cell": "c",
    "paste_cell_above": "c-v",
    "paste_cell_below": "v",
    "insert_cell_above": "a",
    "insert_cell_below": "b",
}

# TODO: Read in user bindings as JSON?
user_bindings = {
    "exit_cell_to_command": "z",
}
BINDINGS = {k: user_bindings.get(k, DEFAULT_KEY_BINDINGS.get(k)) for k in DEFAULT_KEY_BINDINGS}


class KeyBindings:

    edit_mode: bool

    def bind_keys(self):
        @Condition
        def edit_mode() -> bool:
            return self.edit_mode

        @Condition
        def command_mode() -> bool:
            return not self.edit_mode

        @self.key_bindings.add(BINDINGS["exit"])
        async def kb_exit(event):
            await self.exit()

        @self.key_bindings.add(BINDINGS["save"], filter=command_mode)
        def kb_save(event):
            self.save()

        @self.key_bindings.add(BINDINGS["enter_cell_to_edit"], filter=command_mode)
        def kb_enter(event):
            self.enter_cell()

        @self.key_bindings.add(BINDINGS["exit_cell_to_command"], filter=edit_mode, eager=True)
        def kb_escape(event):
            self.exit_cell()

        @self.key_bindings.add(BINDINGS["go_up"], filter=command_mode)
        def kb_go_up(event):
            self.go_up()

        @self.key_bindings.add(BINDINGS["go_down"], filter=command_mode)
        def kb_down(event):
            self.go_down()

        @self.key_bindings.add(BINDINGS["move_cell_up"], filter=command_mode)
        def kb_move_up(event):
            self.move_up()

        @self.key_bindings.add(BINDINGS["move_cell_down"], filter=command_mode)
        def kb_move_down(event):
            self.move_down()

        @self.key_bindings.add(BINDINGS["clear_output"], filter=command_mode)
        def kb_clear_output(event):  # noqa
            self.clear_output()

        @self.key_bindings.add(BINDINGS["make_cell_markdown"], filter=command_mode)
        def kb_markdown_cell(event):
            self.markdown_cell()

        @self.key_bindings.add(BINDINGS["make_cell_code"], filter=command_mode)
        def kb_code_cell(event):
            self.code_cell()

        @self.key_bindings.add(BINDINGS["run_cell_and_stay"], filter=command_mode)
        async def kb_queue_run_cell(event):
            await self.queue_run_cell()

        @self.key_bindings.add(BINDINGS["run_cell_and_select_below"], filter=command_mode)
        async def kb_queue_run_cell_and_select_below(event):
            await self.queue_run_cell(and_select_below=True)

        @self.key_bindings.add(BINDINGS["cut_cell"], filter=command_mode)
        def kb_cut_cell(event):
            self.cut_cell()

        @self.key_bindings.add(BINDINGS["copy_cell"], filter=command_mode)
        def kb_copy_cell(event):
            self.copy_cell()

        @self.key_bindings.add(BINDINGS["paste_cell_above"], filter=command_mode)
        def kb_paste_cell(event):
            self.paste_cell()

        @self.key_bindings.add(BINDINGS["paste_cell_below"], filter=command_mode)
        def kb_paste_cell_under(event):
            self.paste_cell(below=True)

        @self.key_bindings.add(BINDINGS["insert_cell_above"], filter=command_mode)
        def kb_insert_cell(event):
            self.insert_cell()

        @self.key_bindings.add(BINDINGS["insert_cell_below"], filter=command_mode)
        def kb_insert_cell_bellow(event):
            self.insert_cell(below=True)
