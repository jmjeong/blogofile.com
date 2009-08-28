(add-to-list 'load-path "_emacs/")

(require 'htmlize)
(require 'org)

;(global-font-lock-mode t)
(prefer-coding-system 'utf-8)
(add-to-list 'auto-mode-alist '("\\.\\(org\\)$" . org-mode))
;(message "loaded")