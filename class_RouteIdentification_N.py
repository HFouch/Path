from class_DefineRearrangementOperations import DefineRearrangementOperations
from class_RearrangementOperationExecution import RearrangementOperationExecution
from class_SequenceBlockAndEdgeSeriesIdentification import SequenceBlockAndEdgeSeriesIdentification
from class_final_tranlocation_search_N import FinalTranslocationSearch


class RouteIdentification:


    is_last_operation = 0

    def __init__(self):
        pass

    def __del__(self):
        pass

    def identify_routes(self, sequence_blocks, route, Paths, level):


        generate_the_series_of_edges = SequenceBlockAndEdgeSeriesIdentification()
        edge_series = generate_the_series_of_edges.generate_edge_series(sequence_blocks)


        find_rearrangement_operations = DefineRearrangementOperations()
        Inversions = find_rearrangement_operations.inversion_identification(edge_series)
        Raw_Translocations = find_rearrangement_operations.translocation_identification(edge_series, sequence_blocks)
        Translocations = find_rearrangement_operations.removal_of_equivalent_translocations(Raw_Translocations, sequence_blocks)


        Inverted_translocations = find_rearrangement_operations.inverted_translocation_identification(edge_series,
                                                                                                    sequence_blocks)



        Operations = []
        Operations.extend(Inversions)
        Operations.extend(Translocations)
        Operations.extend(Inverted_translocations)
        if len(Operations) != 0:
          Operations.append('Catch_all')

        print()
        print('Level: ', level)
        print('Operations:   ', Operations)
        print()


        find_routes = RouteIdentification()


        if len(edge_series) == 0:
           # print('Finalised route')
          #  print('Level: ', level)
           # print('Route:  ', route)
          #  print('Route length, ', len(route))
           # print()

            #print('Removed route:  ', route)
           # print()

            Paths.append(route[:])
           # print('Paths:   ', Paths)
            if route[-1] == 'FINAL_INVERSIONS':
               # print('Route before popping invs:   ', route)
                route.pop()
                route.pop()

               # print('Route after popping invs:    ', route)


            elif route[-1] == 'FINAL_TRANSLOCATIONS':
               # print('Route before popping TRNS:   ', route)
                route.pop()
                route.pop()

               # print('Route after popping TRNS:    ', route)

            route.pop()
            level -= 1
            #print('Level: ', level)
            #print('Route end pop():   ', route)
           # print()



            pass

        elif len(Operations) == 0:
          #  print()
           # print('No more operations!')
           # print()
            final_inversions = []
            search_final_inversions = find_rearrangement_operations.final_inversion_search(sequence_blocks,
                                                                                           final_inversions)

            new_sequence_blocks = search_final_inversions[0]
            inversions_found = search_final_inversions[1]

           # print('Iversions found:   ', inversions_found)
           # print()
            if len(inversions_found) != 0:

               # print('Route prior:   ', route)
                route.append(final_inversions[:])
                route.append(('FINAL_INVERSIONS'))
                level += 1
               # print()
               # print('Route post:    ', route)
               # print()
               # print('Level:  ', level)
               # print()

                find_routes.identify_routes(new_sequence_blocks, route, Paths, level)
            else:
                #print('LOOKING FOR TRANSLOCATIONS!!!')
                find_translocations = FinalTranslocationSearch()
                list_of_final_translocations  = []
                blocks = []
                search_final_tranlocations = find_translocations.final_translocation_search(sequence_blocks, blocks, list_of_final_translocations)
                new_sequence_blocks = search_final_tranlocations[0]
                translocations_found = search_final_tranlocations[1]
               # print('Translocations found:  ', translocations_found)
              #  print()

                if len(translocations_found) != 0:
                   # print('Route prior  to trns: ', route)
                    final_translocations = []
                    for i in range(len(translocations_found)):
                        final_translocations.append(translocations_found[i][0])

                    route.append(final_translocations[:])
                    route.append('FINAL_TRANSLOCATIONS')

                   # print('Route after trns:  ',route)
                   # print('SB after final translocation,  ', new_sequence_blocks)
                    find_routes.identify_routes(new_sequence_blocks, route, Paths, level)

                else:
                    print('FD sequence_blocks:   ', sequence_blocks)
                    Paths.append(route[:])
                    route.pop()
                    level -= 1
                    pass





        else:
            level += 1
            for i in range(len(Operations)):
                current_opperation = Operations[i]

                if current_opperation == 'Catch_all':

                    if level == 1:
                        break



                    else:
                       # print()
                       # print('It has been caught..    ')
                        #print()

                        if route[-1] == 'FINAL_INVERSIONS':
                           # print('Route before popping invs:   ', route)
                            route.pop()
                            route.pop()
                           # print('Route after popping invs:    ', route)


                        elif route[-1] =='FINAL_TRANSLOCATIONS':
                           # print('Route before popping TRNS:   ', route)
                            route.pop()
                            route.pop()
                          #  print('Route after popping TRNS:    ', route)



                       # print()
                       # print('Route before:    ', route)
                        route.pop()
                        level -= 1
                       # print('Route after:     ', route)
                       # print()

                        pass


                else:
                    excecute_operation = RearrangementOperationExecution()
                    excecute = excecute_operation.execute_operations(current_opperation, Inversions, Translocations,
                                                                Inverted_translocations, sequence_blocks)

                    new_sequence_blocks = excecute[0]
                    route.append(excecute[1])

                    find_routes.identify_routes(new_sequence_blocks, route, Paths, level)

        return Paths




