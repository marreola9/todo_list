import unittest
import tkinter as tk
from unittest.mock import MagicMock

from todo import Todo


class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = Todo(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_add_valid_task(self):
        self.app.selected_tasks = ["Task1", "Task2"]
        self.app.task_frame.insert = MagicMock()
        self.app.add_task_handler(tk.Toplevel(), "Task1")
        self.assertTrue("Task1" in self.app.tasks)
        self.app.task_frame.insert.assert_called_once_with(tk.END, "Task1")

    def test_add_invalid_task(self):
        self.app.selected_tasks = ["Task1", "Task2"]
        self.app.task_frame.insert = MagicMock()
        self.app.add_task_handler(tk.Toplevel(), "Task3")
        self.assertFalse("Task3" in self.app.tasks)
        self.app.task_frame.insert.assert_not_called()

    def test_delete_task(self):
        self.app.task_frame.delete = MagicMock()
        self.app.tasks = ["Task1", "Task2", "Task3"]
        self.app.task_frame.curselection = MagicMock(return_value=(1, 2))
        self.app.delete_task()
        self.assertEqual(self.app.tasks, ["Task1"])
        self.app.task_frame.delete.assert_any_call(2)
        self.app.task_frame.delete.assert_any_call(1)

    def test_update_selected_tasks(self):
        self.app.task_frame.curselection = MagicMock(return_value=(0, 1))
        self.app.update_selected_tasks(None)
        self.assertEqual(self.app.selected_tasks, ["Running", "Walk Dog", "Clean Room", "Shopping", "Research", "Call Mom", "Workout", "Swimming", "Sleeping", "Reading", "Studying", "Netflix"])


if __name__ == "__main__":
    unittest.main()