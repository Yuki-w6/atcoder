FROM rust:1.89

WORKDIR /mnt

RUN apt-get update && \
    apt-get install -y \
    bash \
    git \
    bash-completion \
    && rm -rf /var/lib/apt/lists/*

RUN cargo install cargo-compete --version 0.10.7 --locked

# bash をデフォルトシェルとして設定
SHELL ["/bin/bash", "-c"]

CMD ["tail", "-f", "/dev/null"]
