from src.environment import GridEnvironment
from src.planner import AStarPlanner
from src.agent import Agent
from src.visualization import visualize

def main():
    env = GridEnvironment(20, 20)
    start = (0, 0)
    goal = (19, 19)

    planner = AStarPlanner(env.grid)
    path = planner.find_path(start, goal)

    agent = Agent(start, path)

    visualize(env.grid, path, start, goal)

if __name__ == "__main__":
    main()