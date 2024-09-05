"""
----------------------------------------------------------------------------------------------------------------------------------
Name: Nishanth Senthil Kumar
Roll No: EE23B049
Date: 4th August 2024
Description: Spice Circuit solver, solves circuits with resistors and independant voltage and current sources
Input: filename (String)
Output: 2 dictionaries, first one contains nodes as the keys and the node voltages as the values, and the second
one contains current through the voltage sources, the key is name of the voltage source and the value is the 
current through the voltage sources. 
----------------------------------------------------------------------------------------------------------------------------------
"""

import numpy as np

def valid_filename(filename: str) -> None:
    """
    Checks if the file name is valid by attempting to open it.

    Args:
        filename (str): The name of the file to check.

    Raises:
        FileNotFoundError: If the file cannot be found.
    """
    try:
        with open(filename, "r") as f:
            pass
    except FileNotFoundError:
        raise FileNotFoundError("Please give the name of a valid SPICE file as input")


def valid_fileinput_checker(filename: str)-> None:
    """

    Description: Checks to make sure if the file is not malformed (should contain '.circuit' and '.end')
    Input: filename(String)
    Output: Returns 0 if the file is invalid, returns 1 otherwise

    """

    f = open(filename, "r")
    data = f.read()

    # checking for the valid conditions
    if ".circuit" not in data:
        return 0

    if ".end" not in data:
        return 0

    return 1


def parser(filename: str) -> tuple[dict, int]:
    """
    Parses the SPICE file to create a node graph and count voltage sources.

    Args:
        filename (str): The path to the SPICE file.

    Returns:
        tuple[dict, int]: The node graph and the number of voltage sources.

    Raises:
        ValueError: If the file contains unknown components or is malformed.
    """

    # node_graph stores the adjacency list with the nodes and the nodes with which it is connected to, along with the circuit elements
    node_graph = dict()

    # opening the file
    f = open(filename, "r")
    x = f.readline()

    # voltage_source counts the number of voltage sources in the circuit
    voltage_sources = 0

    # start is a boolean which checks if '.circuit' has been reached by f.readline(), parsing starts when it start becomes True
    start = False

    while ".end" not in x:
        x = x.strip("\n")

        # updating start when it reaches '.circuit'
        if ".circuit" in x:
            start = True
            x = f.readline()

        # reading until it reaches '.circuit'
        elif not start:
            x = f.readline()

        elif start and x:
            # processing the data
            components = x.strip("\n").split(" ")
            i = 0

            # removing empty spaces that are extra in the input
            for elem in components:
                if elem == "":
                    components.pop(i)
                i = i + 1

            branch1 = []
            branch2 = []
            line_check = []

            # this ensures all the unnessary extra data is removed from the list (like stray comments)
            for elem in components:
                if elem != "":
                    line_check.append(elem)
            del components

            components = list(line_check)

            # raising error if there are non V,I,R elements in the file
            if components[0][0].upper() not in "RIV":
                raise ValueError("Only V, I, R elements are permitted")

            # A resistor should have 4 arguments, the name, nodes it is connected to and the value, raises error if it doesnt have this
            if components[0][0].upper() == "R":

                if len(components) < 4:
                    raise ValueError("Malformed circuit file")

                components = list(components[0:4])

            # a V or I source should have 5 arguments, the name, nodes it is connected to, dc or ac and the value, raises error if it doesnt have this
            if components[0][0].upper() == "I" or components[0][0].upper() == "V":

                if len(components) < 5:
                    raise ValueError("Malformed circuit file")

                components = list(components[0:5])

            # branch1 and branch2 contains details on each of the circuit elements, they get added to the dictionary with its first and second node being the key respectively
            branch2.append(components[0])
            branch2.append(components[1])
            branch2.append(components[-1])

            if components[0][0].upper() == "V":
                pass

                branch2[2] = -1 * float((components[-1]))

            # counting the number of voltage sources
            if components[0][0].upper() == "V":
                voltage_sources += 1

            branch1.append(components[0])
            branch1.append(components[2])
            branch1.append(components[-1])

            if components[0][0].upper() == "I":
                branch1[2] = -1 * float((components[-1]))

            # initialising the dictionary
            if components[1] not in node_graph.keys():
                node_graph[components[1]] = []

            if components[2] not in node_graph.keys():
                node_graph[components[2]] = []

            node_graph[components[1]].append(branch1)
            node_graph[components[2]].append(branch2)

            x = f.readline()
        else:
            x = f.readline()

    # closing the file
    f.close()

    # returning the adjacency list and number of voltage sources
    return node_graph, voltage_sources


def valid_circuit(A: np.ndarray) -> bool:
    """
    Checks if the circuit is solvable based on the nodal equation matrix.

    Args:
        nodal_matrix (np.ndarray): The matrix representing the nodal equations.

    Returns:
        bool: True if the matrix is solvable (i.e., its rank is equal to its size), 
              False otherwise.
    """
    # comparing ranks instead of finding determinant to avoid floating point errors
    if np.linalg.matrix_rank(A) < A.shape[0]:
        return 0

    return 1


def evalSpice(filename):

    # checks if the filename is valid
    valid_filename(filename)

    # checks if the fileinput is valid and throws error if it is not valid
    valid_input = valid_fileinput_checker(filename)

    if not valid_input:
        raise ValueError("Malformed circuit file")

    # voltage sources stores the number of voltage sources present in the circuit
    voltage_sources = list(parser(filename))[1]

    # node graph stores the adjacency list containing the graph represented by the circuit
    node_graph = list(parser(filename))[0]
    node_graph = {key: node_graph[key] for key in sorted(node_graph)}

    # node_graph_2 is just a copy of the same graph, which will be required later
    node_graph_2 = list(parser(filename))[0]
    node_graph_2 = {key: node_graph_2[key] for key in sorted(node_graph_2)}

    # raising error if a ground(reference node) is not defined
    if "GND" not in list(map(lambda x: x.upper(), node_graph.keys())):
        raise ValueError(("Malformed circuit file"))

    # voltage list stores the different voltage sources in the circuit in order,
    voltage_list = []

    for i in node_graph:
        for j in node_graph[i]:
            if j[0][0].upper() == "V":
                voltage_list.append(j[0])

    seen = set()
    unique_voltage_list = []
    for voltage in voltage_list:
        if voltage not in seen:
            unique_voltage_list.append(voltage)
            seen.add(voltage)

    # making sure there are no duplicate terms and that they are in order
    del voltage_list
    voltage_list = list(unique_voltage_list)

    # deleting the ground node as it is not required, would simplify data processing
    del node_graph["GND"]
    del node_graph_2["GND"]

    # these two dictionaries give every node (except the reference node) a label from 0 to n-1 and every number from 0 to n-1 to a node
    # n here is the number of nodes (apart from the reference nodes)
    node_mapping_list = dict()
    node_back_mapping_list = dict()

    i = 0
    for keys in node_graph.keys():
        node_mapping_list[i] = keys
        node_back_mapping_list[keys] = i
        i = i + 1

    # since we had deleted the ground node, the number of nodes in the circuit is the number of keys in the graph
    unsolved_nodes = len(node_graph.keys())

    # generating the G matrix, n*n matrix, diagonal elements have sum of conductances connected to ith node
    # off diagonal elements (i,j) and (j,i) are the conductances between ith and jth nodes
    # error is raised when the given resistance is 0, which is not possible

    G = np.zeros((unsolved_nodes, unsolved_nodes))

    for i in range(unsolved_nodes):
        diagonal_conductance = 0
        for j in node_graph[node_mapping_list[i]]:
            if float(j[2]) == 0 and j[0][0].upper() == "R":
                raise ValueError(
                    "Resistance cant be equal to 0, Please check your input"
                )

            elif j[0][0].upper() == "R" and float((j[2])) != 0:
                diagonal_conductance += 1 / float((j[2]))

        G[i][i] = diagonal_conductance

    for i in range(unsolved_nodes):

        for j in node_graph[node_mapping_list[i]]:
            if j[0][0].upper() == "R" and j[1].upper() != "GND":
                G[i][node_back_mapping_list[j[1]]] = -1 / float((j[2]))
                G[node_back_mapping_list[j[1]]][i] = -1 / float((j[2]))

    # B matrix is filled using the polairty of the independant voltage sources
    B = np.zeros((unsolved_nodes, voltage_sources))

    k = 0

    # Filling of B matrix has 2 cases, when one of the voltage sources is connected to gnd, one element gets added
    # If one of the voltage sources is connected to nodes which are not GND, two elements get populated
    for i in node_graph:
        for j in node_graph[i]:
            if j[0][0].upper() == "V" and j[1].upper() != "GND":
                branch1 = node_graph[j[1]]

                if j[1].upper() != "GND":

                    for m in branch1:

                        if m[0][0].upper() == "V" and m[1] == i:
                            if float((j[2])) >= 0:
                                B[node_back_mapping_list[i]][k] = 1
                                B[node_back_mapping_list[j[1]]][k] = -1

                            else:
                                B[node_back_mapping_list[i]][k] = -1
                                B[node_back_mapping_list[j[1]]][k] = 1

                        m[0] = "R"
                        j[0] = "R"

            if j[0][0].upper() == "V" and j[1].upper() == "GND":
                if float((j[2])) >= 0:

                    B[node_back_mapping_list[i]][k] = 1

                elif float(j[2]) < 0 and j[1].upper() == "GND":
                    B[node_back_mapping_list[i]][k] = -1

                else:
                    B[node_back_mapping_list[i]][k] = -1

                j[0] = "R"
                k += 1

    # this checks the polarity of the voltage source, if positive terminal is connected to GND, 'True' is appended
    # This 'True' flag is used later to multiply a factor of -1
    for i in node_graph_2:
        for j in node_graph_2[i]:
            if float(j[2]) < 0 and j[1].upper() == "GND":
                j.append("True")

    # C is the transpose of B if only independant sources are present in the circuit
    C = np.zeros((voltage_sources, unsolved_nodes))
    for i in range(voltage_sources):
        for j in range(unsolved_nodes):
            C[i][j] = B[j][i]

    # D is full of zeros for resistive and independant source circuit (m*m matrix)
    D = np.zeros((voltage_sources, voltage_sources))

    # the A matrix is constructed by appending G,B,C,D horizontally, then vertically
    top = np.hstack((G, B))
    bottom = np.hstack((C, D))
    A = np.vstack((top, bottom))

    # the current_at_nodes dictionary stores the net current flowing into each node from independant current sources
    current_at_nodes = dict()
    for i in node_graph_2:
        total_current = 0

        for j in node_graph_2[i]:
            if j[0][0].upper() == "I":

                total_current += float(j[2])

        current_at_nodes[i] = total_current
        total_current = 0

    # I is part of the Z matrix, has the net current flowing into each node
    I = np.zeros((unsolved_nodes, 1))

    # sorting it so that it can be mapped easily
    current_at_nodes = {key: current_at_nodes[key] for key in sorted(current_at_nodes)}
    for i in current_at_nodes:
        I[node_back_mapping_list[i]][0] = float(current_at_nodes[i])

    # E is the bottom half of the Z matrix, consists of the values of the voltage sources
    E = np.zeros((voltage_sources, 1))
    k = 0

    # depending on whether the negative flag is raised, the sign of the voltage values are decided
    for i in node_graph_2:
        for j in node_graph_2[i]:

            if j[0][0].upper() == "V":
                if j[-1] == "True":
                    E[k][0] = abs(float((j[2])))

                else:
                    E[k][0] = float((j[2]))

                k += 1
            if k >= voltage_sources:
                break
        if k >= voltage_sources:
            break

    # Z is the RHS matrix,
    Z = np.vstack((I, E))

    # checking for invalid circuit conditions, and throws an error is it is invalid
    valid_matrix = valid_circuit(A)

    if valid_matrix == 0:
        raise ValueError("Circuit error: no solution")

    # solving the linear equation matrices
    X = np.linalg.solve(A, Z)

    # these two dictionaries store the final answers, node_ans contains node as key, and voltage at the node as value (in Volts)
    # current ans has the current flowing through a voltage source as the valuex
    node_ans = dict()
    current_ans = dict()
    j = 0

    # updating final answer
    for i in range(len(node_graph.keys())):
        node_ans[list(node_graph.keys())[i]] = X[j][0]
        j += 1

    # updating final answer
    for i in range(len(voltage_list)):
        current_ans[voltage_list[i]] = X[j][0]
        j += 1

    # adding the ground node, which was deleted before as it was not used
    node_ans["GND"] = float(0)
    node_ans = {key: node_ans[key] for key in sorted(node_ans)}

    # returning the answer
    return node_ans, current_ans


