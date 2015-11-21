
call lessc styles.less styles.css

call lessc --clean-css="--compatibility=ie8 --advanced" styles.less styles.min.css

call copy /Y styles.css ..\static\css\styles.css
call copy /Y styles.min.css ..\static\css\styles.min.css
