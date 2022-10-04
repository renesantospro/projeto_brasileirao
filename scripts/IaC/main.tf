# aws_s3_bucket.bucket:
resource "aws_s3_bucket" "bucket" {
    bucket                      = "mkdocs-deployment-testing-with-github"
    object_lock_enabled         = false
    policy                      = jsonencode(
        {
            Id        = "S3PolicyId1"
            Statement = [
                {
                    Action    = "s3:*"
                    Effect    = "Allow"
                    Principal = "*"
                    Resource  = "arn:aws:s3:::mkdocs-deployment-testing-with-github/*"
                    Sid       = "IPAllow"
                },
            ]
            Version   = "2012-10-17"
        }
    )
    
    request_payer               = "BucketOwner"
    tags                        = {}
    tags_all                    = {}
    

    grant {
        permissions = [
            "READ",
        ]
        type        = "Group"
        uri         = "http://acs.amazonaws.com/groups/global/AllUsers"
    }
    grant {
        id          = "05403dc8702ec559f26c38b16e47de3692fbec79b385ed297cf33c3270a7626d"
        permissions = [
            "FULL_CONTROL",
        ]
        type        = "CanonicalUser"
    }

    server_side_encryption_configuration {
        rule {
            bucket_key_enabled = false

            apply_server_side_encryption_by_default {
                sse_algorithm = "AES256"
            }
        }
    }

    timeouts {}

    versioning {
        enabled    = false
        mfa_delete = false
    }

    website {
        error_document = "404.html"
        index_document = "index.html"
    }
}
