# Degrees Harvard SC50 AI
import csv
import sys
import util


from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    # directory = sys.argv[1] if len(sys.argv) == 2 else "large"
    directory = sys.argv[1] if len(sys.argv) == 2 else "small"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    # print(source)
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")
    # print(target)
    print(f"Names: {names}")
    print(f"People: {people}")
    print(f"Movies: {movies}")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    print(f"Source: {source}")
    print(f"Target: {target}")

    # Get neighbours
    neighbours = neighbors_for_person(source)
    print(f"Neighbours: {neighbours}")
    first_state = [f_state for f_state in neighbours if f_state[1] == source][0]
    print(f"First State: {first_state}")
    action = set([n_star[1] for n_star in neighbours if n_star[1] != source])
    print(f"Connected stars: {action}")

    parent_node = None
    q_frontier = util.QueueFrontier()
    q_frontier.add(Node(first_state, parent_node, action))
    action.add(source)
    found_stars = action
    # result format [(Movie 2, "Actor 2"), ("Movie 1", "Actor 1"), (Movie 3, "Actor 3")]
    # !? node((Movie, actor_id), parent_node, (next_movie_id, next_person_id))
    target_found = False
    degree = 0
    while True:
        removed_node = q_frontier.remove()
        degree += 1
        for current_star in removed_node.action:
            neighbours = neighbors_for_person(current_star)
            action = set([n[1] for n in neighbours if n[1] not in found_stars])
            found_stars.union(action)
            for parent in [p for p in neighbours if p[1] == current_star]:
                for state in [s for s in neighbours if parent[0] == s[0] and s[1] != parent[1]]:
                    if state[1] == target:
                        link = removed_node.parent
                        path = [state]
                        while link is not None:
                            path.append(link.state)
                            link = link.parent

                        print(f"Path: {path}")
                        return path

                    q_frontier.add(util.Node(state, parent, action))
        if degree == 6:
            return None

    # raise NotImplementedError


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
