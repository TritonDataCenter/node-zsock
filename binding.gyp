{
  "targets": [
    {
      "target_name": "zsock",
      "sources": [
        "src/zsock.cc"
      ],
      "ldflags": [
        "-lpthread",
        "-lcontract",
        "-lnsl",
        "-lsocket"
      ],
      "cflags_cc": [
        "-D_POSIX_C_SOURCE=200112L",
        "-DSunOS",
        "-Wall",
        "-fPIC"
      ]
    }
  ]
}
