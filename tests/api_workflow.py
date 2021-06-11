def run_api_workflow_with_assertions(workflow_specification, current_request, test_context):
    current_request_result = current_request(test_context)
    if current_request_result is not None and current_request_result["continue_workflow"]:
        run_api_workflow_with_assertions(
            workflow_specification,
            workflow_specification[current_request_result["next_request"]],
            test_context
        )
