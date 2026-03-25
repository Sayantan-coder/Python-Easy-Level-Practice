def get_sum_budget(List: list) -> int:
    budget_list = []
    for persons in List:
        budget_list.append(persons["budget"])
    total_budget = sum(budget_list)
    return total_budget


print(
    get_sum_budget(
        [
            {"name": "sayantan", "age": 22, "budget": 18000},
            {"name": "suman", "age": 20, "budget": 15000},
            {"name": "souvik", "age": 22, "budget": 15000},
            {"name": "proloy", "age": 28, "budget": 18000},
        ]
    )
)
