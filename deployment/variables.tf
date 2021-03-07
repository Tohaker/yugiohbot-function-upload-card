variable "function_title" {
  description = "The name of the function."
  default     = "yugiohbot__card-uploader"
}

variable "function_name" {
  description = "The name of the function archive."
  default     = "function"
}

variable "function_description" {
  description = "The description of the function."
  default     = "Social Media card uploader for the YuGiOhBot"
}

variable "function_runtime" {
  description = "The runtime for the function."
  default     = "python38"
}

variable "entry_point" {
  description = "The name of the function to run from main.py"
  default     = "function"
}

variable "access_token" {
  description = "The Facebook access token to allow posting to the page."
}

variable "service_account" {
  description = "The name of the service account that is allowed to invoke the function."
  default     = "621027686268-compute@developer.gserviceaccount.com"
}