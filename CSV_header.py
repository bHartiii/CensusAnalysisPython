class IndiaCensusCSV:
    def __init__(self):
        self.state = "State"
        self.population = "Population"
        self.area = "AreaInSqKm"
        self.density = "DensityPerSqKm"

    def __repr__(self):
        """
        :return: header of IndiaCensusCsv file
        """
        return self.state + "," + self.population + "," + self.area + "," + self.density
