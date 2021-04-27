from prompt_toolkit.filters import Condition


class KeyBindings:

    edit_mode: bool

    def bind_keys(self):
        @Condition
        def edit_mode() -> bool:
            return self.edit_mode

        @Condition
        def command_mode() -> bool:
            return not self.edit_mode

        @self.key_bindings.add("c-q")
        async def kb_exit(event):
            await self.exit()

        @self.key_bindings.add("c-s", filter=command_mode)
        def kb_save(event):
            self.save()

        @self.key_bindings.add("enter", filter=command_mode)
        def kb_enter(event):
            self.enter_cell()

        @self.key_bindings.add("escape", filter=edit_mode, eager=True)
        def kb_escape(event):
            self.exit_cell()

        @self.key_bindings.add("up", filter=command_mode)
        def kb_go_up(event):
            self.go_up()

        @self.key_bindings.add("down", filter=command_mode)
        def kb_down(event):
            self.go_down()

        @self.key_bindings.add("c-up", filter=command_mode)
        def kb_move_up(event):
            self.move_up()

        @self.key_bindings.add("c-down", filter=command_mode)
        def kb_move_down(event):
            self.move_down()

        @self.key_bindings.add("l", filter=command_mode)
        def kb_clear_output(event):  # noqa
            self.clear_output()

        @self.key_bindings.add("m", filter=command_mode)
        def kb_markdown_cell(event):
            self.markdown_cell()

        @self.key_bindings.add("o", filter=command_mode)
        def kb_code_cell(event):
            self.code_cell()

        @self.key_bindings.add("c-e", filter=command_mode)
        async def kb_queue_run_cell(event):
            await self.queue_run_cell()

        @self.key_bindings.add("c-r", filter=command_mode)
        async def kb_queue_run_cell_and_select_below(event):
            await self.queue_run_cell(and_select_below=True)

        @self.key_bindings.add("x", filter=command_mode)
        def kb_cut_cell(event):
            self.cut_cell()

        @self.key_bindings.add("c", filter=command_mode)
        def kb_copy_cell(event):
            self.copy_cell()

        @self.key_bindings.add("c-v", filter=command_mode)
        def kb_paste_cell(event):
            self.paste_cell()

        @self.key_bindings.add("v", filter=command_mode)
        def kb_paste_cell_under(event):
            self.paste_cell(below=True)

        @self.key_bindings.add("a", filter=command_mode)
        def kb_insert_cell(event):
            self.insert_cell()

        @self.key_bindings.add("b", filter=command_mode)
        def kb_insert_cell_bellow(event):
            self.insert_cell(below=True)
