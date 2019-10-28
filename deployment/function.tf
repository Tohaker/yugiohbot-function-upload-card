resource "google_cloudfunctions_function" "function" {
  name        = var.function_title
  description = var.function_description
  runtime     = var.function_runtime

  available_memory_mb   = 512
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.function.name
  timeout               = 120

  entry_point   = var.entry_point
  trigger_http  = true

  environment_variables = {
    ACCESS_TOKEN  = var.access_token
    FB_PAGE_ID    = var.fb_page_id
  }
}

resource "google_cloudfunctions_function_iam_member" "invoker" {
  cloud_function  = google_cloudfunctions_function.function.name
  region          = google_cloudfunctions_function.function.region
  member          = "serviceAccount:${var.service_account}"
  role            = "roles/cloudfunctions.invoker"
}
