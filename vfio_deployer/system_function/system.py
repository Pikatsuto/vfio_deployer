import subprocess


class System:
    def __init__(self):
        """
        Initialize the system class
        """

        self.throw_error = True
        self.return_output = True

        self.pcie = {}

    def shell(self, command):
        """
        Run a shell command and return the output
        :param command: command to run
        :return: None
        """

        # run command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # throw error
        if self.throw_error and error:
            raise Exception(error.decode("utf-8"))

        # return output
        if self.return_output:
            return output.decode("utf-8")

    def get_pcie(self):
        """
        Get the pcie devices
        :return: list of pcie devices
        """

        # get pcie devices
        pcie_lines = self.shell("lspci -nn | grep -E 'VGA|Audio'").split("\n")[:-1]
        for pcie_line in pcie_lines:
            # get pcie device information
            pcie_device = pcie_line.split(" ")[0]
            pcie_family = pcie_device.split(".")[0]
            pcie_description = " ".join(pcie_line.split(" ")[1:])

            # add pcie device to list
            if pcie_family in self.pcie:
                self.pcie[pcie_family].update({
                    pcie_device: pcie_description
                })
            else:
                self.pcie.update({
                    pcie_family: {
                        pcie_device: pcie_description
                    }
                })

        # return output
        return self.pcie
