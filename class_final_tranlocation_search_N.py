from class_SequenceBlockAndEdgeSeriesIdentification import SequenceBlockAndEdgeSeriesIdentification
from class_DefineRearrangementOperations import DefineRearrangementOperations
from class_RearrangementOperationExecution import RearrangementOperationExecution



class FinalTranslocationSearch:

    def __init__(self):
        pass
    def __del__(self):
        pass

    def final_translocation_search(self, sequence_blocks, blocks, list_of_final_translocations):

        generate_the_series_of_edges = SequenceBlockAndEdgeSeriesIdentification()
        find_translocations = FinalTranslocationSearch()
        edge_series = generate_the_series_of_edges.generate_edge_series(sequence_blocks)


       # print()
       # print('Edge series:  ', edge_series)
       # print('Sequence blocks:   ', sequence_blocks)
       # print('list of final trns:   ', list_of_final_translocations)
       # print('blocks:   ', blocks)
       # print()

       # print('len(edge_series):  ', len(edge_series))
       # print()
        if len(edge_series) == 0:
            #print('IT IS NOW ZERO')
            return sequence_blocks, list_of_final_translocations


        while len(edge_series) != 0:
            new_translocations = []

            while len(new_translocations) == 0:
                #print('Is executing')
        #new_translocations = []
                i = 0
        #while len(new_translocations) == 0:
            #if len(edge_series) == 0:
               # print('IT IS NOW ZERO')
                #break

            #elif i > len(edge_series) - 1:
             #   print('i TOO BIG:  ', i)

            #else:
                while i < len(edge_series):
                  #  print('i:  ', i)
                    current_edge = edge_series[i]
                    search_for_translocations = find_translocations.translocation_search(current_edge, sequence_blocks,
                                                                                         blocks)

                    new_sequence_blocks = search_for_translocations[0]
                    blocks = search_for_translocations[1]
                    new_translocations = search_for_translocations[2]

                    if len(new_translocations) == 0:
                        i += 1

                    else:
                        list_of_final_translocations.append(new_translocations)
                        sequence_blocks = new_sequence_blocks
                        edge_series = generate_the_series_of_edges.generate_edge_series(sequence_blocks)


                        return find_translocations.final_translocation_search(sequence_blocks, blocks,
                                                                       list_of_final_translocations)

                else:
                   # print('ES and ES len:  ' , edge_series, len(edge_series))
                   # print('block removal is executing')


                    block_removal = find_translocations.perform_block_removal(edge_series, sequence_blocks, blocks)
                    edge_series = block_removal[0]
                    sequence_blocks = block_removal[1]
                    blocks = block_removal[2]

                   # print()
                   # print('edge_series after block removal:  ', edge_series)
                   # print('sequence blocks after block removal:   ', sequence_blocks)
                   # print('blocks after block removal:  ', blocks)
                   # print()

                    return find_translocations.final_translocation_search( sequence_blocks, blocks,
                                                                   list_of_final_translocations)

       # else:

            #list_of_final_translocations.append(new_translocations)
           # sequence_blocks = new_sequence_blocks
            #edge_series = generate_the_series_of_edges.generate_edge_series(sequence_blocks)
           # find_translocations.final_translocation_search(edge_series, sequence_blocks, blocks,
            #                                               list_of_final_translocations)

       # if len(edge_series) != 0:
       #     print('block removal is executing')
       #     block_removal = find_translocations.perform_block_removal(edge_series, sequence_blocks, blocks)
       #     edge_series = block_removal[0]
       #     sequence_blocks = block_removal[1]
       #     blocks = block_removal[2]

       #     print()
       #     print('edge_series after block removal:  ', edge_series)
       #     print('sequence blocks after block removal:   ', sequence_blocks)
       #     print('blocks after block removal:  ', blocks)
       #     print()
       #    find_translocations.final_translocation_search(edge_series, sequence_blocks, blocks,
       #                                                    list_of_final_translocations)

        #return sequence_blocks, list_of_final_translocations

    def translocation_search(self, current_edge_pair, sequence_blocks, blocks):

        execute_translocation = RearrangementOperationExecution()
        list_of_translocations = []
        blocks_list = []
        for i in range(len(blocks)):
            blocks_list.append((blocks[i][0], blocks[i][-1]))
       # print('block list:  ', blocks_list)
        i = 0

        edge1 = current_edge_pair[0]
        edge2 = current_edge_pair[1]

        compatible_sequence_block_1 = (abs(edge1) + 1)
        compatible_sequence_block_2 = (abs(edge2) - 1)

        compatible_sequence_block = (int(compatible_sequence_block_1), int(compatible_sequence_block_2))
        #print('   compatible sequence block  ', compatible_sequence_block)

        if compatible_sequence_block[0] in sequence_blocks and compatible_sequence_block[1] in sequence_blocks:
            position_block1 = sequence_blocks.index(compatible_sequence_block[0])
            position_block2 = sequence_blocks.index(compatible_sequence_block[1])
            position_edge1 = sequence_blocks.index(edge1)

            if position_block1 < position_block2 and position_edge1 not in range(position_block1,
                                                                                 position_block2):
                translocation = (current_edge_pair, compatible_sequence_block)
                add_to_list = ('TRN', current_edge_pair, compatible_sequence_block)
                list_of_translocations.append(add_to_list)
                execute = execute_translocation.excecute_translocation(translocation, sequence_blocks)
                sequence_blocks = execute[0]



            elif position_block1 == position_block2:
               # print('single block')
                translocation = (current_edge_pair, compatible_sequence_block)
                add_to_list = ('TRN', current_edge_pair, compatible_sequence_block)
                list_of_translocations.append(add_to_list)
                execute = execute_translocation.excecute_translocation(translocation, sequence_blocks)
                sequence_blocks = execute[0]
               # print('new sequence blocks:  ', sequence_blocks)






        elif compatible_sequence_block in blocks_list:
            block_position = blocks_list.index(compatible_sequence_block)
            #print()
            #print('found in blocks')
            new_sequence_blocks = sequence_blocks[:sequence_blocks.index(current_edge_pair[0]) + 1] + blocks[
                block_position] + sequence_blocks[sequence_blocks.index(current_edge_pair[0]) + 1:]
            sequence_blocks = new_sequence_blocks
            # sequence_blocks.insert(sequence_blocks.index(current_edge_pair[0])+1, blocks[block_position])
           # print('new sequence blocks, ', sequence_blocks)
            add_to_list = ('TRN', current_edge_pair, (blocks[i][0], blocks[i][-1]))
            list_of_translocations.append(add_to_list)
            blocks.remove(blocks[i])

        return sequence_blocks, blocks, list_of_translocations

    def perform_block_removal(self, edge_series, sequence_blocks, blocks):
       # print()
       # print('block removal is seriously executing... (-_-)')
        #print('edge s:  ', edge_series)
       # print('sequence blocks:  ',sequence_blocks)
        block_to_remove = sequence_blocks[
                          sequence_blocks.index(edge_series[0][1]):sequence_blocks.index(edge_series[1][0]) + 1]
        #print()
       # print('edges:  ', edge_series[0], edge_series[1])
       # print('block to be removed:  ', block_to_remove)
        blocks.append(block_to_remove)
        for i in range(len(block_to_remove)):
            sequence_blocks.remove(block_to_remove[i])

       # print()
       # print('blocks:  ', blocks)
       # print()
       # print('sequence blocks:  ', sequence_blocks)
       # print()

        generate_the_series_of_edges = SequenceBlockAndEdgeSeriesIdentification()
        edge_series = generate_the_series_of_edges.generate_edge_series(sequence_blocks)

        return edge_series, sequence_blocks, blocks

    def dfinal_translocation_search(self, sequence_blocks, edge_series, blocks, list_of_final_translocations):

        while len(edge_series) > 1:
            print('NOW')
            block_to_remove = sequence_blocks[
                              sequence_blocks.index(edge_series[0][1]):sequence_blocks.index(edge_series[1][0]) + 1]
            print()
            print('edges:  ', edge_series[0], edge_series[1])
            print('block to be removed:  ', block_to_remove)
            blocks.append(block_to_remove)
            for i in range(len(block_to_remove)):
                sequence_blocks.remove(block_to_remove[i])

            print()
            print('blocks:  ', blocks)
            print()
            print('sequence blocks:  ', sequence_blocks)
            print()

            generate_the_series_of_edges = EdgeSeriesAndSequenceBlocks()
            edge_series = generate_the_series_of_edges.GenerateEdgesSeries(sequence_blocks)

            find_translocations = RearrangementOperationIdentification()
            final_translocations = find_translocations.find_final_translocations(edge_series, sequence_blocks, blocks)
            sequence_blocks = final_translocations[0]
            print('new sb:  ', sequence_blocks)
            translocation = final_translocations[1]
            print('translocation:  ', translocation)
            blocks = final_translocations[2]
            print('blocks:  ', blocks)

            edge_series = generate_the_series_of_edges.GenerateEdgesSeries(sequence_blocks)

            # if len(translocation) != 0:
            #   list_of_final_translocations.append(translocation)
            #   generate_the_series_of_edges = EdgeSeriesAndSequenceBlocks()
            #   edge_series = generate_the_series_of_edges.GenerateEdgesSeries(sequence_blocks)
            # find_translocations.final_translocation_search(sequence_blocks,edge_series,blocks,list_of_final_translocations)

        return sequence_blocks, list_of_final_translocations

    def find_final_translocations(self, edge_series, sequence_blocks, blocks):
        execute_translocation = RearrangementOperationExcecution()
        found_translocation = []
        blocks_list = []
        for i in range(len(blocks)):
            blocks_list.append((blocks[i][0], blocks[i][-1]))
        print('block list:  ', blocks_list)

        i = 0
        while i < len(edge_series):

            # for edge_pair in range(len(edge_series)):

            # current_edge_pair = edge_series[edge_pair]
            current_edge_pair = edge_series[i]
            print()
            print('    current edge pair  ', current_edge_pair)

            edge1 = current_edge_pair[0]
            edge2 = current_edge_pair[1]

            compatible_sequence_block_1 = (abs(edge1) + 1)
            compatible_sequence_block_2 = (abs(edge2) - 1)

            compatible_sequence_block = (int(compatible_sequence_block_1), int(compatible_sequence_block_2))
            print('   compatible sequence block  ', compatible_sequence_block)

            if compatible_sequence_block[0] in sequence_blocks and compatible_sequence_block[1] in sequence_blocks:
                position_block1 = sequence_blocks.index(compatible_sequence_block[0])
                position_block2 = sequence_blocks.index(compatible_sequence_block[1])
                position_edge1 = sequence_blocks.index(edge1)

                if position_block1 < position_block2 and position_edge1 not in range(position_block1, position_block2):
                    translocation = (current_edge_pair, compatible_sequence_block)
                    found_translocation.append(('TRN', translocation))
                    execute = execute_translocation.excecute_translocation(translocation, sequence_blocks)
                    sequence_blocks = execute[0]

                elif position_block1 == position_block2:
                    print('single block')
                    translocation = (current_edge_pair, compatible_sequence_block)
                    found_translocation.append(('TRN', translocation))
                    execute = execute_translocation.excecute_translocation(translocation, sequence_blocks)
                    sequence_blocks = execute[0]
                    print('new sequence blocks:  ', sequence_blocks)

                break


            elif compatible_sequence_block in blocks_list:
                block_position = blocks_list.index(compatible_sequence_block)
                print()
                print('found in blocks')
                sequence_blocks.insert(sequence_blocks.index(current_edge_pair[0]), blocks[block_position])
                print('new sequence blocks, ', sequence_blocks)
                found_translocation = (('TRN', current_edge_pair, (blocks[i][0], blocks[i][-1])))
                blocks.remove(blocks[i])

                break





            else:
                i += 1

        return sequence_blocks, found_translocation, blocks




