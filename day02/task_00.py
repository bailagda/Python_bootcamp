class key:
    passphrase = "zax2rulez"
    def __len__(self):
        return 1337

    def __getitem__(self, key):
        return 3

    def __gt__(self, other):
        if other == 9000:
            return True

    def __str__(self):
        return "GeneralTsoKeycard"