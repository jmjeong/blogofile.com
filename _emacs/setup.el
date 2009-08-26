(add-to-list 'load-path "_emacs/")

(require 'htmlize)
(require 'org)
;(require 'color-theme)

(global-font-lock-mode t)

(add-to-list 'auto-mode-alist '("\\.\\(org\\)$" . org-mode))
(message "loaded")