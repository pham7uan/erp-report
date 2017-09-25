
def linear_regression(xArray,yArray):
        # if (xArray.length != yArray.length)
        #     return null;

        MAXN = xArray.__len__()
        n = 0

        # first pass: read in data, compute xbar and ybar
        sumx = 0.0
        sumy = 0.0
        sumx2 = 0.0

        x = [];
        y = [];

        for k in range(0,MAXN):
            x.append(xArray[k]);
            y.append(yArray[k]);
            sumx += x[n];
            sumx2 += x[n] * x[n];
            sumy += y[n];
            n = n+1


        xbar = sumx / n;
        ybar = sumy / n;

        # second pass: compute summary statistics
        xxbar = 0.0
        yybar = 0.0
        xybar = 0.0
        for h in range(0,n):
            xxbar += (x[h] - xbar) * (x[h] - xbar);
            yybar += (y[h] - ybar) * (y[h] - ybar);
            xybar += (x[h] - xbar) * (y[h] - ybar);

        beta1 = xybar / xxbar;
        beta0 = ybar - beta1 * xbar;

        # print results
        # print("y   = " + str(beta1) + " * x + " + str(beta0));


        #generate result
        entryPoints = {}
        line =[]

        for k in range(0,MAXN):
            y0 = beta1 * k + beta0;
            entryPoints[k] = {k:y0};
            line.append(y0)

        # print line
        return line

# yArray =[233,200,160,160,160,160,160,160,160,160,160,160]
# xArray =[0,1,2,3,4,5,6,7,8,9,10,11]
# linear_regression(xArray,yArray)