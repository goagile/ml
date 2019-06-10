import numpy
from scipy.special import expit as sigmoid


class NeuroNet:

    def __init__(self, inp_nodes, hid_nodes, out_nodes, learning_rate):
        self.inp = inp_nodes
        self.hid = hid_nodes
        self.out = out_nodes
        self.rate = learning_rate
        self.Wih = numpy.random.normal(0.0, pow(self.hid, -0.5), (self.hid, self.inp))
        self.Who = numpy.random.normal(0.0, pow(self.out, -0.5), (self.out, self.hid))
        self.F = sigmoid

    def train(self, inp_list, targ_list):
        I = numpy.array(inp_list, ndmin=2).T
        T = numpy.array(targ_list, ndmin=2).T

        I_h = numpy.dot(self.Wih, I)
        Out_h = self.F(I_h)

        I_f = numpy.dot(self.Who, Out_h)
        Out_f = self.F(I_f)

        E = T - Out_f
        E_h = numpy.dot(self.Who.T, E)

        self.Who += self.rate * numpy.dot(
            (E * Out * (1.0 - Out_f)),
            numpy.transpose(Out_h))

        self.Wih += self.rate * numpy.dot(
            (E_h * Out_h * (1.0 - Out_h)),
            numpy.transpose(I))

        pass

    def query(self, inp_list):
        I = numpy.array(inp_list, ndmin=2).T

        I_h = numpy.dot(self.Wih, I)
        Out_h = self.F(I_h)

        I_f = numpy.dot(self.Who, Out_h)
        Out_f = self.F(I_f)

        return Out_f


if __name__ == "__main__":

    net = NeuroNet(
        inp_nodes=3,
        hid_nodes=3,
        out_nodes=3,
        learning_rate=0.3)

    q = net.query([1.0, 0.5, -1.5])
    print(q)

