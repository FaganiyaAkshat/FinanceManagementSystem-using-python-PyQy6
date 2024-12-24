self.frame_4.hide()
self.pushButton_2.clicked.connect(self.addvoting)
self.pushButton_4.clicked.connect(self.submitvoting)


def addvoting(self):
    self.frame_4.show()
    self.frame_8.hide()


def submitvoting(self):
    self.frame_4.hide()
    self.frame_8.show()