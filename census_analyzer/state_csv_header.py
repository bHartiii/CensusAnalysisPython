class StateCSVHeader:
    def __init__(self):
        self.sr_no = "SrNo"
        self.state = "State Name"
        self.tin = "TIN"
        self.code = "StateCode"

    def __repr__(self):
        return self.sr_no + "," + self.state + "," + self.tin + "," + self.code
