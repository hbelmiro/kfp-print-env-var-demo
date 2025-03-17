FROM quay.io/fedora/python-311

LABEL org.opencontainers.image.source="https://github.com/hbelmiro/kfp-print-env-var-demo/blob/main/Containerfile"

ENV MY_ENV_VAR="my_value"