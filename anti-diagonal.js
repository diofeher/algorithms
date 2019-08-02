arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

function test(arr) {
    var N = arr.length;
    B = [];
    for (var i=0; i < (N * 2) - 1; i++) {
        B[i] = [];
    }
    console.log('B:', B);

    for(var column=N, row=0; column > 0; column--, row++) {
        var k=row;
        // console.log('row:', row, 'column:', column);
        for(var i=0; i < column; i++) {
            // console.log('k', k, 'linha:', i, 'item:', arr[row][i]);
            B[k].push( arr[row][i] );
            k += 1;
        }

        for(var i=row+1; i < N; i++) {
            // console.log('k', k, 'coluna:', i, 'item:', arr[i][column-1]);
            B[k].push( arr[i][column-1] );
            k += 1;
        }
    }
    
    console.log('B:', B);
    return B;
}

test(arr);