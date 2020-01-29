class operation:

    def blend(self, image, logo, x=None, y=None, alpha=None):
        '''
                Use logo and blend it on the image at location (x, y)
                image: the original image
                logo: the logo to blend on to the image
                x: topleft coordinate x
                y: topleft coordinate y
                alpha: blend ratio to the logo

                returns the image blended with logo at loction (x, y)
                '''
        y1o, y2o = max(0, -y), min(logo.shape[1], image.shape[1] - x)
        x1o, x2o = max(0, -x), min(logo.shape[0], image.shape[0] - y)
        y1, y2 = max(0, y), min(image.shape[1], x + logo.shape[0])
        x1, x2 = max(0, x), min(image.shape[0], y + logo.shape[1])

        if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
            return

        for c in range(3):
            image[y1:y2, x1:x2] = (alpha * logo[y1o:y2o, x1o:x2o] + (1 - alpha) * image[y1:y2, x1:x2])

            return image

