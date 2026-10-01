group "default" {
    targets = ["calculadora"]
}

target "calculadora" {
    context = "."
    dockerfile = "Dockerfile"

    tags = [
        "calculadora-validacion:latest"
    ]
}