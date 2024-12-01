from neo4j import GraphDatabase


class GraphService:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def save_node(self, lemma, part_of_speech):
        query = """
        MERGE (n:Word {lemma: $lemma, part_of_speech: $part_of_speech})
        RETURN n
        """
        with self.driver.session() as session:
            session.run(query, lemma=lemma, part_of_speech=part_of_speech)

    def get_all_nodes(self):
        query = """
        MATCH (n:Word)
        RETURN n.lemma AS lemma, n.part_of_speech AS part_of_speech
        """
        with self.driver.session() as session:
            result = session.run(query)
            return [record for record in result]
