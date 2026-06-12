class BaseManager:

    def __init__(self):

        self.active = True

    # ====================================
    # ENABLE
    # ====================================

    def enable(self):

        self.active = True

    # ====================================
    # DISABLE
    # ====================================

    def disable(self):

        self.active = False