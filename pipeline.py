from kfp import dsl


@dsl.component(base_image="quay.io/hbelmiro/kfp-print-env-var-demo:latest")
def comp(env_var: str) -> str:
    import os

    value = os.getenv(env_var, "default")
    print(value)
    return value


@dsl.pipeline
def my_pipeline(env_var: str) -> str:
    return comp(env_var=env_var).output
