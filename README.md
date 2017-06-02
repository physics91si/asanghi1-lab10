## Feedback

* Good!
* Minor style detail: if you find yourself doing `if` statements with returning `True` or `False`, you can often make it cleaner (e.g. lines 10-13 can be written as `return element in self.set`)
* For the `__or__` method, it's almost good, but we don't want duplicate entries in our set
